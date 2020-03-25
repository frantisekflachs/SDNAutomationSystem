from mininet.topo import Topo


class Topology2(Topo):
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        # hosts
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')

        # switches
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')

        # links
        self.addLink(host1, switch1)
        self.addLink(host2, switch1)
        self.addLink(host3, switch2)
        self.addLink(host4, switch2)
        self.addLink(switch1, switch2)


topos = {'topology2': (lambda: Topology2())}
