from mininet.topo import Topo


class Network1(Topo):
    """ h1 --- s1 --- h2 """

    def build(self):

        # hosts
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')

        # switches
        switch1 = self.addSwitch('s1')

        # links
        self.addLink(host1, switch1)
        self.addLink(host2, switch1)


topos = {'network1': (lambda: Network1())}
