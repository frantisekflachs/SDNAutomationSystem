from mininet.topo import Topo
from mininet.node import Node


class LinuxRouter(Node):
    """ A Node with IP forwarding enabled. """

    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        # Enable forwarding on the router
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()


class Network4(Topo):
    """ r0 --- s1 --- h1-1, h1-2, h1-3
           --- s2 --- h2-1, h2-2, h2-3
           --- s3 --- h3-1, h3-2, h3-3 """

    def build(self):
        defaultIP = '192.168.0.1/24'  # IP address for r0-eth1
        router = self.addNode('r0', cls=LinuxRouter, ip=defaultIP)

        s1, s2, s3 = [self.addSwitch(s) for s in ('s1', 's2', 's3')]

        self.addLink(s1, router, intfName2='r0-eth1', params2={'ip': defaultIP})  # for clarity
        self.addLink(s2, router, intfName2='r0-eth2', params2={'ip': '172.16.0.1/16'})
        self.addLink(s3, router, intfName2='r0-eth3', params2={'ip': '10.0.0.1/8'})

        h11 = self.addHost('h1-1', ip='192.168.0.100/24', defaultRoute='via 192.168.0.1')
        h12 = self.addHost('h1-2', ip='192.168.0.101/24', defaultRoute='via 192.168.0.1')
        h13 = self.addHost('h1-3', ip='192.168.0.102/24', defaultRoute='via 192.168.0.1')

        h21 = self.addHost('h2-1', ip='172.16.0.100/16', defaultRoute='via 172.16.0.1')
        h22 = self.addHost('h2-2', ip='172.16.0.101/16', defaultRoute='via 172.16.0.1')
        h23 = self.addHost('h2-3', ip='172.16.0.102/16', defaultRoute='via 172.16.0.1')

        h31 = self.addHost('h3-1', ip='10.0.0.100/8', defaultRoute='via 10.0.0.1')
        h32 = self.addHost('h3-2', ip='10.0.0.101/8', defaultRoute='via 10.0.0.1')
        h33 = self.addHost('h3-3', ip='10.0.0.102/8', defaultRoute='via 10.0.0.1')

        for h, s in [(h11, s1), (h12, s1), (h13, s1),
                     (h21, s2), (h22, s2), (h23, s2),
                     (h31, s3), (h32, s3), (h33, s3)]:
            self.addLink(h, s)


topos = {'network4': (lambda: Network4())}
