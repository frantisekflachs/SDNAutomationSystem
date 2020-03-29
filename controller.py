from topology_tests.test_executor import TestExecutor

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

        # binding listeners on buttons
        pub.subscribe(self.runTopology, "btnRunTopology_Pressed")
        pub.subscribe(self.endTopology, "btnEndTopology_Pressed")
        pub.subscribe(self.showSDNControllerGui, "btnSDNControllerGui_Pressed")
        pub.subscribe(self.testTopology, "btnTestTopology_Pressed")

    def runTopology(self):
        """Load configure and run SDN Automation System"""

        # load SDN controller
        self.loadedSDNController = self.loadSDNController()
        if self.loadedSDNController is None:
            self.view.printText("Error reading SDN Controller.")
            return
        self.view.printText("SDN Controller loaded.")

        # load topology
        self.loadedTopologyTemplate = self.loadTopology()
        if self.loadedTopologyTemplate is None:
            self.view.printText("Topology template not selected.")
            return
        self.view.printText("Topology template yaml loaded.")

        # load settings from yaml file
        self.topologyTests, self.networkTemplate, self.networkSetup, self.SDNControllerSetup = self.model.loadTopologyConfig("topology_templates_config/{}.yaml".format(self.loadedTopologyTemplate), self.loadedSDNController)

        if (self.topologyTests or self.networkTemplate or self.networkSetup or self.SDNControllerSetup) is None:
            self.view.printText("Error reading topology config file.")
            return
        self.view.printText("Topology settings from yaml loaded.")

        # run SDN controller
        self.model.runSDNController(self.loadedSDNController, self.SDNControllerSetup)
        self.view.printText("SDN Controller started.")

        # sleep for 6 sec
        time.sleep(6)

        # run network topology
        self.xtermEnable = self.loadXTermEnable()
        if self.xtermEnable:
            self.networkSetup.append('-x')

        self.model.runVirtualNetwork(self.networkTemplate, self.networkSetup)

        self.topologyState = "RUNNING"
        self.view.printText("Virtual network is running.")
        self.view.printText("Topology is running.")

    def endTopology(self):
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
            self.view.printText('Testing topology... wait ' + str(len(self.topologyTests)*5) + ' sec')

            self.testExecutor = TestExecutor(self.loadedSDNController)
            testsResults = self.testExecutor.run(self.topologyTests)

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
            selectedTopologyTemplate = self.view.getSelectedTopologyTemplate()
            topology = config.implementedTopologyTemplates[selectedTopologyTemplate]
            return topology
        except:
            return None

    def loadXTermEnable(self):
        """Load enabling of XTerm fo all hosts"""

        try:
            xterm = self.view.getXTerm()
            return xterm
        except:
            return None
