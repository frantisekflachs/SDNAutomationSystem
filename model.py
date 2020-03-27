from networkTopology.virtualTopology.mininetVirtualTopology import MininetVirtualTopology
import config
import yaml


class Model:
    """ Model for the MVC architecture. """

    def loadTopologyConfig(self, topologyConfigPath, SDNController):
        """Load topology from yaml config file
        topologyPath: path where to find config file"""

        # TODO except missing parameters
        try:
            stream = open(topologyConfigPath, 'r')
            loadedTopologyConfig = yaml.load(stream, Loader=yaml.FullLoader)

            tt = loadedTopologyConfig["topologyTests"]
            nt = loadedTopologyConfig["networkTemplate"]
            # ipb = loadedTopologyConfig["IPBase"]
            ns = loadedTopologyConfig['networkSetup']
            # nofv = loadedTopologyConfig['networkOFVersion']
            sdns = loadedTopologyConfig[config.implementedSDNControllersNames[config.implementedSDNControllersClasses.index(SDNController)]]

            return tt, nt, ns, sdns

        except:
            return None

    def runSDNController(self, SDNController, SDNControllerSetup):
        """Run SDN Controller
        SDNController: Implemented SDN Controllers in the system."""

        SDNController.run(self, SDNControllerSetup)

    def runVirtualNetwork(self, networkTemplate, networkSetup):
        """Run Network Topology
        topology: pre-defined topology
        topologyIP: IP address pool
        SDNControllerIP: IP address for the controller"""

        mvt = MininetVirtualTopology(networkTemplate, networkSetup)
        mvt.run()

    def showSDNControllerGui(self, SDNController):
        """Show SDN Controller GUI"""
        SDNController.showSDNControllerGui(self)
