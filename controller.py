from pubsub import *
import time

import config
from post_configurations.post_config_executor import PostConfigExecutor


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

        # self.testExecutor = None
        self.topologyState = "STOPPED"

        # binding listeners on buttons
        pub.subscribe(self.runTopology, "btnRunTopology_Pressed")
        pub.subscribe(self.endTopology, "btnEndTopology_Pressed")
        pub.subscribe(self.showSDNControllerGui, "btnSDNControllerGui_Pressed")
        pub.subscribe(self.testTopology, "btnTestTopology_Pressed")
        pub.subscribe(self.runSDNController, "btnRunSDNController_Pressed")
        pub.subscribe(self.runVirtualNetwork, "btnRunVirtualNetwork_Pressed")
        pub.subscribe(self.runSelfDefinedScript, "btnRunScript_Pressed")
        pub.subscribe(self.loadSDNCTopologyTemplate, "topologyTemplate_Changed")

    def runTopology(self):
        """Load configure and run SDN Automation System"""

        try:
            # load parameter from GUI defined by user
            self.loadParametersFromGUI()

            # RUN SDN CONTROLLER
            self.model.runSDNController(self.loadedSDNController, self.SDNControllerSetup)
            self.view.printTextLog("SDN Controller started.")

            # sleep for 10 sec
            time.sleep(10)

            # RUN VIRTUAL NETWORK
            self.model.runVirtualNetwork(self.loadedTopologyTemplate, self.xtermEnable)
            self.view.printTextLog("Virtual network started.")

            self.topologyState = "RUNNING"
            self.view.printTextLog("Topology is running.")

            # sleep for 10 sec
            time.sleep(10)

            # load topology tests to GUI lists
            self.view.loadImplementedTopologyTests(self.topologyTests)

            # post config topology
            self.runPostConfigSetup(self.postConfig, self.loadedSDNController)

        except Exception as e:
            print("Something went wrong " + str(e))

    def runSDNController(self):
        """Run choosen SDN Controller"""

        try:
            # load parameter from GUI defined by user
            self.loadParametersFromGUI()

            self.model.runSDNController(self.loadedSDNController, self.SDNControllerSetup)
            self.view.printTextLog("SDN Controller started.")

            # load topology tests to GUI lists
            self.view.loadImplementedTopologyTests(self.topologyTests)

            # post config topology
            self.runPostConfigSetup(self.postConfig, self.loadedSDNController)

            self.topologyState = "RUNNING"
            self.view.printTextLog("Topology is running.")

        except Exception as e:
            print("Something went wrong " + str(e))

    def runVirtualNetwork(self):
        """Run choosen virtual network"""

        try:
            # load parameter from GUI defined by user
            self.loadParametersFromGUI2()

            self.model.runVirtualNetwork(self.loadedTopologyTemplate, self.xtermEnable)
            self.view.printTextLog("Virtual network started.")

            # load topology tests to GUI lists
            self.view.loadImplementedTopologyTests(self.topologyTests)

            # post config topology
            self.runPostConfigSetup(self.postConfig, self.loadedSDNController)

            self.topologyState = "RUNNING"
            self.view.printTextLog("Topology is running.")

        except Exception as e:
            print("Something went wrong " + str(e))

    def endTopology(self):
        """End all created instances for SDN Controller nad virtual network"""

        try:
            self.model.endTopology()
            self.view.printTextLog("Topology was ended.")
        except Exception as e:
            print("Something went wrong " + str(e))

    def showSDNControllerGui(self):
        """Show SDN Controller GUI"""

        try:
            c = self.loadSDNController()
            if c is not None:
                self.view.printTextLog('Opening SDN GUI')
                self.model.showSDNControllerGui(c)
            else:
                self.view.printTextLog('No SDN Controller for GUI choosed.')
        except Exception as e:
            print("Something went wrong " + str(e))

    def testTopology(self):
        """Test choosen topology with loaded tests"""

        try:
            if self.topologyState is "STOPPED":
                self.view.printTextLog('Topology not started.')
            else:
                self.view.printTextLog('Testing topology... ' + str(len(self.topologyTests) * 6) + ' sec')
                testsResults = self.model.testTopology(self.loadedSDNController, self.topologyTests)
                self.view.printTextTopologyTests(testsResults)
        except Exception as e:
            print("Something went wrong " + str(e))

    def runPostConfigSetup(self, postConfig, sdnc):
        """Run SDN Controller post config setup
        postConfig: loaded post configuration for choosen topology
        sdnc: loaded SDN Controller"""

        try:
            pce = PostConfigExecutor(sdnc)
            ret = pce.run(postConfig)
            self.view.printTextLog('Post config sucess: ' + str(ret))
        except Exception as e:
            print("Something went wrong " + str(e))

    def runSelfDefinedScript(self):
        """Run script defined in gui by user"""

        try:
            scriptName = self.view.getScriptName()
            self.model.runSelfDefinedScript(scriptName)
        except Exception as e:
            print("Something went wrong " + str(e))

    def loadParametersFromGUI(self):
        """Load parameter defined bz user from GUI"""

        try:
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
            self.view.printTextLog("Topology {} template loaded.".format(self.loadedTopologyTemplate))

            # load settings from yaml file
            self.topologyTests, self.networkTemplate, self.SDNControllerSetup, self.postConfig = self.model.loadTopologyConfig(
                "topology_templates/{}".format(self.loadedTopologyTemplate), self.loadedSDNController)

            if (self.topologyTests or self.networkTemplate or self.SDNControllerSetup) is None:
                self.view.printTextLog("Error reading topology {} config file.".format(self.loadedTopologyTemplate))
                return
            self.view.printTextLog("Topology settings from {} loaded.".format(self.loadedTopologyTemplate))

            # check xterm enable in GUI
            self.xtermEnable = self.loadXTermEnable()
        except Exception as e:
            print("Something went wrong " + str(e))

    def loadParametersFromGUI2(self):
        """Load parameter defined bz user from GUI"""

        try:
            # load SDN controller
            self.loadedSDNController = None

            # load topology
            self.loadedTopologyTemplate = self.loadTopology()
            if self.loadedTopologyTemplate is None:
                self.view.printTextLog("Topology template not selected.")
                return
            self.view.printTextLog("Topology {} template loaded.".format(self.loadedTopologyTemplate))

            # load settings from yaml file
            self.topologyTests, self.networkTemplate, self.SDNControllerSetup, self.postConfig = self.model.loadTopologyConfig(
                "topology_templates/{}".format(self.loadedTopologyTemplate), self.loadedSDNController)

            if (self.topologyTests or self.networkTemplate) is None:
                self.view.printTextLog("Error reading topology {} config file.".format(self.loadedTopologyTemplate))
                return
            self.view.printTextLog("Topology settings from {} loaded.".format(self.loadedTopologyTemplate))

            # check xterm enable in GUI
            self.xtermEnable = self.loadXTermEnable()
        except Exception as e:
            print("Something went wrong " + str(e))

    def loadSDNController(self):
        """"Load SDN Controller from View"""

        try:
            selectedSDNController = self.view.getSelectedSDNController()
            SDNController = config.implementedSDNControllers[selectedSDNController]
            return SDNController
        except Exception as e:
            print("Something went wrong " + str(e))
            return None

    def loadTopology(self):
        """Load topology from View"""

        try:
            selectedTopologyTemplate = self.view.getSelectedTopologyTemplate()
            return selectedTopologyTemplate
        except Exception as e:
            print("Something went wrong " + str(e))
            return None

    def loadXTermEnable(self):
        """Load enabling of XTerm fo all hosts"""

        try:
            xterm = self.view.getXTerm()
            if xterm:
                return 'enable'
            else:
                return 'disable'
        except Exception as e:
            print("Something went wrong " + str(e))
            return 'disable'

    def loadSDNCTopologyTemplate(self):
        """Load SDNC in topology template and list them in view"""

        try:
            choosedTopoTemplate = self.view.getSelectedTopologyTemplate()
            if choosedTopoTemplate is None:
                self.view.printTextLog("Topology is not selected.")
                return
            sdncInTemplate = self.model.loadSDNCTopologyTemplate(
                "topology_templates/{}".format(choosedTopoTemplate))
            self.view.loadImplementedSDNControllers(sdncInTemplate)
        except Exception as e:
            print("Something went wrong " + str(e))
            return 'disable'
