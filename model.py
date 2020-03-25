from networkTopology.virtualTopology.mininetVirtualTopology import MininetVirtualTopology
import yaml


class Model:
    """ Model for the MVC architecture. """

    def loadTopologyConfig(self, topologyConfigPath):
        """Load topology from yaml config file
        topologyPath: path where to find config file"""

        try:
            stream = open(topologyConfigPath, 'r')
            loadedTopologyConfig = yaml.load(stream, Loader=yaml.FullLoader)

            topologyTemplate = loadedTopologyConfig["topologyTemplate"]
            IPAddressPool = loadedTopologyConfig["IPAddressPool"]
            tests = loadedTopologyConfig["tests"]

            return topologyTemplate, IPAddressPool, tests
        except:
            return None

    def runSDNController(self, SDNController, OFVersion):
        """Run SDN Controller
        SDNController: Implemented SDN Controllers in the system.
        OFVerson: OpenFlow protocol version"""

        SDNController.run(self, OFVersion)

    def runNetworkTopology(self, topology, topologyIP, OFVersion, SDNControllerIP):
        """Run Network Topology
        topology: pre-defined topology
        topologyIP: IP address pool
        SDNControllerIP: IP address for the controller"""

        mvt = MininetVirtualTopology(topology, topologyIP, OFVersion, SDNControllerIP)
        mvt.run()

    def showSDNControllerGui(self, SDNController):
        """Show SDN Controller GUI"""
        SDNController.showSDNControllerGui(self)
