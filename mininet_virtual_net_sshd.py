import sys
from functools import partial
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import lg, info
from mininet.node import Node, RemoteController, OVSKernelSwitch
from mininet.util import waitListening
import config


def MyNetwork(params):
    """Create My Network from loaded parameters."""

    try:
        topo = config.implementedVirtualNetworks[params[0]]
        switch = partial(OVSKernelSwitch, protocols='OpenFlow{}'.format(params[1]))

        # if last param is x, then run with XTerm for each host, x is loaded from GUI
        if params[-1] == 'x':
            x = True
        else:
            x = False

        return Mininet(topo, controller=lambda name: RemoteController(name, ip='127.0.0.1'), switch=switch, xterms=x, ipBase='192.168.0.0/24', cleanup=True)
    except Exception as e:
        print("Something went wrong " + str(e))


def connectToRootNS(network, switch, ip, routes):
    """Connect hosts to root namespace via switch. Starts network.
      network: Mininet() network object
      switch: switch to connect to root namespace
      ip: IP address for root namespace node
      routes: host networks to route to"""

    try:
        # Create a node in root namespace and link to s1
        root = Node('root', inNamespace=False)
        intf = network.addLink(root, switch).intf1
        root.setIP(ip, intf=intf)

        # Start network that now includes link to root namespace
        network.start()

        # Add routes from root ns to hosts
        for route in routes:
            root.cmd('route add -net ' + route + ' dev ' + str(intf))
    except Exception as e:
        print("Something went wrong " + str(e))


def sshd(network, ip='10.123.123.1/32', routes=None, switch=None):
    """Start a network, connect it to root ns, and run sshd on all hosts.
       ip: root-eth0 IP address in root namespace (10.123.123.1/32)
       routes: Mininet host networks to route to (10.0/24)
       switch: Mininet switch to connect to root namespace (s1)"""

    try:
        if not switch:
            switch = network['s1']  # switch to use

        if not routes:
            routes = ['10.0.0.0/8', '172.16.0.0/16', '192.168.0.0/24']

        connectToRootNS(network, switch, '192.168.0.200/32', routes)

        for host in network.hosts:
            host.cmd('/usr/sbin/sshd -D -o UseDNS=no -u0 &')

        info("*** Waiting for ssh daemons to start\n")
        for server in network.hosts:
            waitListening(server=server, port=22, timeout=5)

        info("\n*** Hosts are running sshd at the following addresses:\n")
        for host in network.hosts:
            info(host.name, host.IP(), '\n')

        info("\n*** Type 'exit' or control-D to shut down network\n")

        CLI(network)

        info("\n*** Stopping sshd.\n")
        for host in network.hosts:
            host.cmd('kill %/usr/sbin/sshd')

        network.stop()
    except Exception as e:
        print("Something went wrong " + str(e))


if __name__ == '__main__':
    lg.setLogLevel('info')

    net = MyNetwork(sys.argv[1:]) # argv[1:] only params without script name
    sshd(net)
