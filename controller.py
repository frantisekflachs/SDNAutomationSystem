import os
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
        pub.subscribe(self.runSDNController, "btnRunSDNController_Pressed")
        pub.subscribe(self.runVirtualNetwork, "btnRunVirtualNetwork_Pressed")

    def runTopology(self):
        """Load configure and run SDN Automation System"""

        try:
            # load parameter from GUI defined by user
            self.loadParametersFromGUI()

            # run SDN controller
            self.runSDNController()

            # sleep for 6 sec
            time.sleep(6)

            # run virtual network
            self.runVirtualNetwork()

            self.topologyState = "RUNNING"
            self.view.printTextLog("Topology is running.")

            # load topology tests to GUI lists
            self.view.loadImplementedTopologyTests(self.topologyTests)

            # post config topology
            # self.runPostConfigSetup(self.postConfig)

        except:
            self.view.printTextLog("Error running topology.")

    def runSDNController(self):
        """Run SDN Controller
        loadedSDNController: SDN Controller which was loaded via GUI
        SDNControllerSetup: additional parameters/switches for SDN Controller"""

        try:
            # load parameter from GUI defined by user
            self.loadParametersFromGUI()

            self.model.runSDNController(self.loadedSDNController, self.SDNControllerSetup)
            self.view.printTextLog("SDN Controller started.")

            # load topology tests to GUI lists
            self.view.loadImplementedTopologyTests(self.topologyTests)

        except:
            self.view.printTextLog("Error running SDN controller.")

    def runVirtualNetwork(self):
        """Run virtual network
        networkTemplate: template of the network
        networkSetup: additional parameters/switches for virtual network"""

        try:
            # load parameter from GUI defined by user
            self.loadParametersFromGUI()

            self.model.runVirtualNetwork(self.networkTemplate, self.networkSetup)
            self.view.printTextLog("Virtual network started.")

            # load topology tests to GUI lists
            self.view.loadImplementedTopologyTests(self.topologyTests)

        except:
            self.view.printTextLog("Error running virtual network.")

    def endTopology(self):
        """End all created instances"""

        os.system("sudo kill $(ps aux | grep 'floodlight.jar' | awk '{print $2}')")

        os.system("sudo mn --clean")


    def showSDNControllerGui(self):
        """Show SDN Controller GUI"""

        c = self.loadSDNController()

        if c is not None:
            self.view.printTextLog('Opening SDN GUI')
            self.model.showSDNControllerGui(c)
        else:
            self.view.printTextLog('No SDN Controller for GUI choosed.')

    def testTopology(self):
        """Testing topology"""

        if self.topologyState is "STOPPED":
            self.view.printTextLog('Topology not started.')
        else:
            self.view.printTextLog('Testing topology... ' + str(len(self.topologyTests) * 6) + ' sec')

            self.testExecutor = TestExecutor(self.loadedSDNController)
            testsResults = self.testExecutor.run(self.topologyTests)

            self.view.printTextTopologyTests(testsResults)

    def runPostConfigSetup(self, postConfig):
        # topologyPost = postConfig(self.loadedSDNController)
        # ret = topologyPost.run()
        # self.view.printTextLog(ret)
        pass

    def loadParametersFromGUI(self):
        """Load parameter defined bz user from GUI"""

        # load SDN controller
        self.loadedSDNController = self.loadSDNController()
        if self.loadedSDNController is None:
            self.view.printTextLog("Error reading SDN Controller.")
            return
        self.view.printTextLog("SDN Controller {} loaded.".format(self.loadedSDNController))

        # load topology
        self.loadedTopologyTemplate = self.loadTopology()
        if self.loadedTopologyTemplate is None:
            self.view.printTextLog("Topology template not selected.")
            return
        self.view.printTextLog("Topology {} template yaml loaded.".format(self.loadedTopologyTemplate))

        # load settings from yaml file
        self.topologyTests, self.networkTemplate, self.networkSetup, self.SDNControllerSetup, self.postConfig = self.model.loadTopologyConfig(
            "topology_templates_config/{}".format(self.loadedTopologyTemplate), self.loadedSDNController)

        if (self.topologyTests or self.networkTemplate or self.networkSetup or self.SDNControllerSetup) is None:
            self.view.printTextLog("Error reading topology {} config file.".format(self.loadedTopologyTemplate))
            return
        self.view.printTextLog("Topology settings from {}.yaml loaded.".format(self.loadedTopologyTemplate))

        # check xterm enable in GUI
        self.xtermEnable = self.loadXTermEnable()
        if self.xtermEnable:
            # self.networkSetup.append('-x')
            self.networkSetup.append('x')


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
            # topology = config.implementedTopologyTemplates[selectedTopologyTemplate]
            return selectedTopologyTemplate
        except:
            return None

    def loadXTermEnable(self):
        """Load enabling of XTerm fo all hosts"""

        try:
            xterm = self.view.getXTerm()
            return xterm
        except:
            return None
