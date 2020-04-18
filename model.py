from topology_tests.test_executor import TestExecutor
from virtual_network.mininetVirtualNetwork import MininetVirtualTopology
import config
import yaml


class Model:
    """ Model for the MVC architecture. """

    def loadTopologyConfig(self, topologyTemplateConfigPath, SDNController):
        """Load topology from yaml config file
        topologyTemplateConfigPath: path where to find yaml config file
        SDNController: defined SDN Controller - config will be loaded only for this SDN Controller not others"""

        try:
            stream = open(topologyTemplateConfigPath, 'r')
            loadedTopologyConfig = yaml.load(stream, Loader=yaml.FullLoader)

            tt = loadedTopologyConfig["topologyTests"]
            nt = loadedTopologyConfig["networkTemplate"]
            ns = loadedTopologyConfig['networkSetup']
            sdns = loadedTopologyConfig[config.implementedSDNControllersNames[config.implementedSDNControllersClasses.index(SDNController)]]
            pc = loadedTopologyConfig['sdnControllersPostConfig']
            return tt, nt, ns, sdns, pc

        except Exception as e:
            print("Something went wrong " + str(e))

    def runSDNController(self, SDNController, SDNControllerSetup):
        """Run SDN Controller
        SDNController: Implemented SDN Controllers in the system
        SDNControllerSetup: parameters for SDN Controller"""

        try:
            SDNController.run(self, SDNControllerSetup)
        except Exception as e:
            print("Something went wrong " + str(e))

    def runVirtualNetwork(self, networkTemplate, networkSetup):
        """Run Network Topology
        networkTemplate: pre-defined netwrok template
        networkSetup: parameters for virtual network """

        try:
            mvt = MininetVirtualTopology(networkTemplate, networkSetup)
            mvt.run()
        except Exception as e:
            print("Something went wrong " + str(e))

    def runPostConfigScript(self, postConfigScript):
        """Run script after controller and virtual network is started"""

        try:
            ret = postConfigScript.run()
            return ret
        except Exception as e:
            print("Something went wrong " + str(e))

    def showSDNControllerGui(self, SDNController):
        """Show SDN Controller GUI
        SDNController: run GUI for defined SDN Controller"""

        try:
            SDNController.showSDNControllerGui(self)
        except Exception as e:
            print("Something went wrong " + str(e))

    def testTopology(self, loadedSDNController, topologyTests):
        """Testing topology"""

        try:
            testExecutor = TestExecutor(loadedSDNController)
            testsResults = testExecutor.run(topologyTests)
            return testsResults
        except Exception as e:
            print("Something went wrong " + str(e))
