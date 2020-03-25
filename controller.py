from tests.test_executor import TestExecutor

from pubsub import *
import time
import config


class Controller:
    """ Controller for the MVC architecture. """

    def __init__(self, model, view, parent):
        """Inicializing Controller class
        model: model for MVC architecture
        view: view for MVC architecture
        parent: tkinter master app frame"""
        self.parent = parent
        self.model = model
        self.view = view

        self.testExecutor = None
        self.topologyState = "STOPPED"

        self.topology = None
        self.topologyTemplate = None
        self.IPAddressPool = None
        self.SDNController = None
        self.SDNControllerIP = 'localhost'
        self.OFVersion = None
        self.loadedTests = None

        # binding listeners on buttons
        pub.subscribe(self.runSDNAutomationSystem, "btnRunTopology_Pressed")
        pub.subscribe(self.endSDNAutomationSystem, "btnEndTopology_Pressed")
        pub.subscribe(self.showSDNControllerGui, "btnSDNControllerGui_Pressed")
        pub.subscribe(self.testTopology, "btnTestTopology_Pressed")

    def runSDNAutomationSystem(self):
        """Load configure and run SDN Automation System"""
        # topology

        self.topology = self.loadTopology()
        if self.topology is None:
            self.view.printText("Topology not selected.")
            return

        self.topologyTemplate, self.IPAddressPool, self.loadedTests = self.model.loadTopologyConfig(
            "topologyTemplatesConfig/{}Config.yaml".format(self.topology))
        if (self.topologyTemplate or self.IPAddressPool or self.loadedTests) is None:
            self.view.printText("Error reading topology config file.")
            return

        self.OFVersion = self.loadOFVersion()
        if self.OFVersion is None:
            self.view.printText("Error reading OpenFlow protocol version.")
            return

        # SDN controller
        self.SDNController = self.loadSDNController()
        if self.SDNController is None:
            self.view.printText("Error reading SDN Controller.")
            return

        # run SDN controller
        self.model.runSDNController(self.SDNController, self.OFVersion)
        self.view.printText("SDN Controller started.")

        # sleep for 6 sec
        time.sleep(6)

        # run network topology
        self.model.runNetworkTopology(self.topologyTemplate, self.IPAddressPool, self.OFVersion, self.SDNControllerIP)
        self.view.printText("Topology is running.")

        self.topologyState = "RUNNING"

    def endSDNAutomationSystem(self):
        """End all created instances"""
        pass

    def showSDNControllerGui(self):
        """Show SDN Controller GUI"""

        c = self.loadSDNController()

        if c is not None:
            self.view.printText('Opening SDN GUI')
            self.model.showSDNControllerGui(c)
        else:
            self.view.printText('No SDN Controller for GUI choosed.')

    def testTopology(self):
        """Testing topology"""

        if self.topologyState is "STOPPED":
            self.view.printText('Topology not started.')
        else:
            self.view.printText('Testing topology...')
            self.testExecutor = TestExecutor(self.SDNController)
            testsResults = self.testExecutor.run(self.loadedTests)

            self.view.printText(testsResults)

    def loadSDNController(self):
        """"Load SDN Controller from View"""
        try:
            selectedSDNController = self.view.getSelectedSDNController()
            SDNController = config.implementedSDNControllers[selectedSDNController]
            return SDNController
        except:
            return None

    def loadTopology(self):
        """Load topology from View"""
        try:
            selectedTopologyChoosed = self.view.getSelectedTopologyTemplate()
            topology = config.implementedTopologyTemplates[selectedTopologyChoosed]
            return topology
        except:
            return None

    def loadOFVersion(self):
        """Lod OpenFlow protocol version"""
        try:
            OFVersionChoosed = self.view.getOFVersions()
            OFVersion = config.implementedOFVersions[OFVersionChoosed]
            return OFVersion
        except:
            return None
