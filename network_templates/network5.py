from mininet.topo import Topo
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI


class Network5(Topo):

    def build(self):
        s1, s2, s3 = [self.addSwitch(s) for s in ('s1', 's2', 's3')]

        h1 = self.addHost('h1', ip='192.168.0.100/24', defaultRoute='via 192.168.0.1')
        h2 = self.addHost('h2', ip='172.16.0.100/16', defaultRoute='via 172.16.0.1')
        h3 = self.addHost('h3', ip='10.0.0.100/8', defaultRoute='via 10.0.0.1')

        for h, s in [(h1, s1), (h2, s2), (h3, s3)]:
            self.addLink(h, s)

        self.addLink(s1, s2)
        self.addLink(s2, s3)

        # h1.cmd('/usr/sbin/sshd -D -o UseDNS=no -u0 &')
        # h2.cmd('/usr/sbin/sshd -D -o UseDNS=no -u0 &')
        # h3.cmd('/usr/sbin/sshd -D -o UseDNS=no -u0 &')


topos = {'network5': (lambda: Network5())}
