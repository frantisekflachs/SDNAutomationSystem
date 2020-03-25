from networkTopology.virtualTopology.virtualTopology import VirtualTopology
import os


class MininetVirtualTopology(VirtualTopology):
    """Virtual topology Mininet"""

    def __init__(self, topologyTemplate, topologyIP, OFVersion, SDNControllerIP):
        self.topologyTemplate = topologyTemplate
        self.topologyIP = topologyIP
        self.OFVersion = OFVersion
        self.SDNControllerIP = SDNControllerIP

    def run(self):
        """Run Mininet topology"""
        os.system('gnome-terminal -- bash -c '
                  '"mn --custom topologyTemplates/{}.py --topo {} '
                  '-i {} --controller=remote,ip={},port=6653 '
                  '--switch ovsk,protocols=OpenFlow{} '
                  '&& bash"'.format(self.topologyTemplate,
                                    self.topologyTemplate,
                                    self.topologyIP,
                                    self.SDNControllerIP,
                                    self.OFVersion))

    def run2(self):
        """Create an empty network and add nodes to it."""

        # setLogLevel('info')
        #
        # self.net = Mininet(controller=Controller)
        #
        # info('*** Adding controller\n')
        # # net.addController( 'c0' )
        #
        # info('*** Adding hosts\n')
        # h1 = self.net.addHost('h1', ip='10.0.0.1')
        # h2 = self.net.addHost('h2', ip='10.0.0.2')
        #
        # info('*** Adding switch\n')
        # s3 = self.net.addSwitch('s3')
        #
        # info('*** Creating links\n')
        # self.net.addLink(h1, s3)
        # self.net.addLink(h2, s3)
        #
        # info('*** Starting network\n')
        # self.net.start()
        #
        # info('*** Running CLI\n')
        # CLI(self.net)
        #
        # self.net.stop()
