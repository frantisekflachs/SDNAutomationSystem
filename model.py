from networkTopology.virtualTopology.mininetVirtualTopology import MininetVirtualTopology
import config
import yaml


class Model:
    """ Model for the MVC architecture. """

    def loadTopologyConfig(self, topologyConfigPath, SDNController):
        """Load topology from yaml config file
        topologyPath: path where to find config file"""

        try:
            stream = open(topologyConfigPath, 'r')
            loadedTopologyConfig = yaml.load(stream, Loader=yaml.FullLoader)

            nt = loadedTopologyConfig["networkTemplate"]
            ipb = loadedTopologyConfig["IPBase"]
            ns = loadedTopologyConfig['networkSetup']
            tc = loadedTopologyConfig["topologyTests"]
            sdnc = loadedTopologyConfig[config.implementedSDNControllersNames[config.implementedSDNControllersClasses.index(SDNController)]]
            return nt, ipb, ns, tc, sdnc

        except:
            return None

    def runSDNController(self, SDNController, OFVersion, SDNControllerSetup):
        """Run SDN Controller
        SDNController: Implemented SDN Controllers in the system.
        OFVerson: OpenFlow protocol version"""

        SDNController.run(self, OFVersion, SDNControllerSetup)

    def runNetworkTopology(self, topology, topologyIP, topologySetup, OFVersion, SDNControllerIP):
        """Run Network Topology
        topology: pre-defined topology
        topologyIP: IP address pool
        SDNControllerIP: IP address for the controller"""

        mvt = MininetVirtualTopology(topology, topologyIP, topologySetup, OFVersion, SDNControllerIP)
        mvt.run()

    def showSDNControllerGui(self, SDNController):
        """Show SDN Controller GUI"""
        SDNController.showSDNControllerGui(self)
