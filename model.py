from virtual_network.mininetVirtualNetwork import MininetVirtualTopology
import config
import yaml


class Model:
    """ Model for the MVC architecture. """

    def loadTopologyConfig(self, topologyTemplateConfigPath, SDNController):
        """Load topology from yaml config file
        topologyTemplateConfigPath: path where to find yaml config file
        SDNController: defined SDN Controller - config will be loaded only for this SDN Controller not others"""

        # TODO except missing parameters
        try:
            stream = open(topologyTemplateConfigPath, 'r')
            loadedTopologyConfig = yaml.load(stream, Loader=yaml.FullLoader)

            tt = loadedTopologyConfig["topologyTests"]
            nt = loadedTopologyConfig["networkTemplate"]
            ns = loadedTopologyConfig['networkSetup']
            sdns = loadedTopologyConfig[config.implementedSDNControllersNames[config.implementedSDNControllersClasses.index(SDNController)]]

            return tt, nt, ns, sdns

        except:
            return None

    def runSDNController(self, SDNController, SDNControllerSetup):
        """Run SDN Controller
        SDNController: Implemented SDN Controllers in the system
        SDNControllerSetup: parameters for SDN Controller"""

        SDNController.run(self, SDNControllerSetup)

    def runVirtualNetwork(self, networkTemplate, networkSetup):
        """Run Network Topology
        networkTemplate: pre-defined netwrok template
        networkSetup: parameters for virtual network """

        mvt = MininetVirtualTopology(networkTemplate, networkSetup)
        mvt.run2()

    def showSDNControllerGui(self, SDNController):
        """Show SDN Controller GUI
        SDNController: run GUI for defined SDN Controller"""

        SDNController.showSDNControllerGui(self)
