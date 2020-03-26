from mininet.topo import Topo


class Topology1(Topo):

    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        # hosts
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')

        # switches
        switch1 = self.addSwitch('s1')

        # links
        self.addLink(host1, switch1)
        self.addLink(host2, switch1)
        self.addLink(host3, switch1)


topos = {'topology1': (lambda: Topology1())}
