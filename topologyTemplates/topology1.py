from mininet.topo import Topo
from mininet.topolib import TreeTopo


class Topology1(Topo):

    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        # hosts
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')

        # switches
        switch1 = self.addSwitch('s1')

        # links
        self.addLink(host1, switch1)
        self.addLink(host2, switch1)


topos = {'topology1': (lambda: Topology1())}

if __name__ == '__main__':
    topo = TreeTopo(1, 2)
    t = Topology1(Topo)