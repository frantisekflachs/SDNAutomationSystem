import sys
from functools import partial
import yaml
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import lg, info
from mininet.node import Node, RemoteController, OVSKernelSwitch, IVSSwitch, OVSBridge
from mininet.util import waitListening
import config


def loadNetworkSetup(topologyTemplate):
    """Load topology from yaml config file
    topologyTemplate: topology file name - yaml config file"""

    try:
        stream = open(config.topologyTemplatesConfigPath + '/' + topologyTemplate, 'r')
        loadedTopologyConfig = yaml.load(stream, Loader=yaml.FullLoader)
        networkSetup = loadedTopologyConfig["networkSetup"]
        networkTemplate = loadedTopologyConfig["networkTemplate"]
        return networkSetup, networkTemplate
    except Exception as e:
        print("Something went wrong " + str(e))


def virtualNetwork(networkSetup, networkTemplate):
    """Create My Network from loaded parameters.
    networkSetup: dict with parameters for virtual network
    networkTemplate: network template for virtual network"""

    try:
        try:
            switchType = networkSetup['switchType']
            ofVersion = networkSetup['ofVersion']
            if switchType is 'OVSSwitch':
                switch = partial(OVSKernelSwitch, protocols='OpenFlow{}'.format(ofVersion))
            elif switchType is 'IVSSwitch':
                switch = partial(IVSSwitch, protocols='OpenFlow{}'.format(ofVersion))
            elif switchType is 'OVSBridge':
                switch = partial(OVSBridge, protocols='OpenFlow{}'.format(ofVersion))
            else:
                switch = partial(OVSKernelSwitch, protocols='OpenFlow13')
        except Exception as e:
            print("Something went wrong " + str(e))
            switch = partial(OVSKernelSwitch, protocols='OpenFlow13')

        topo = config.implementedVirtualNetworks[networkTemplate]

        # checking defined values, if not defined in template, set default
        try:
            sdnControllerIp = networkSetup['sdnControllerIp']
        except Exception as e:
            print("Something went wrong " + str(e))
            sdnControllerIp = '127.0.0.1'

        try:
            sdnControllerPort = networkSetup['sdnControllerPort']
        except Exception as e:
            print("Something went wrong " + str(e))
            sdnControllerPort = 6653

        try:
            ipBase = networkSetup['ipBase']
        except Exception as e:
            print("Something went wrong " + str(e))
            ipBase = '10.0.0.0/8'

        try:
            cleanUp = networkSetup['cleanUp']
        except Exception as e:
            print("Something went wrong " + str(e))
            cleanUp = False

        try:
            xterm = networkSetup['xterm']
        except Exception as e:
            print("Something went wrong " + str(e))
            xterm = False

        try:
            inNamespace = networkSetup['inNamespace']
        except Exception as e:
            print("Something went wrong " + str(e))
            inNamespace = False

        try:
            autoSetMacs = networkSetup['autoSetMacs']
        except Exception as e:
            print("Something went wrong " + str(e))
            autoSetMacs = False

        try:
            autoStaticArp = networkSetup['autoStaticArp']
        except Exception as e:
            print("Something went wrong " + str(e))
            autoStaticArp = False

        return Mininet(topo,
                       controller=lambda name: RemoteController(name, ip=sdnControllerIp, port=sdnControllerPort),
                       switch=switch,
                       ipBase=ipBase,
                       cleanup=cleanUp,
                       xterms=xterm,
                       inNamespace=inNamespace,
                       autoSetMacs=autoSetMacs,
                       autoStaticArp=autoStaticArp
                       )

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
            root.cmd('sudo route add -net ' + route + ' dev ' + str(intf))
    except Exception as e:
        print("Something went wrong " + str(e))


def sshd(network, networkSetup):
    """Start a network, connect it to root ns, and run sshd on all hosts.
       network: Mininet() network object
       networkSetup: dict with parameters for virtual network"""

    try:
        switch = network['s1']  # switch to use
        try:
            rootIp = networkSetup['rootIp']
        except:
            print('Missing root IP')
            rootIp = '10.0.0.200/32'

        try:
            routesRoot = networkSetup['routesRoot']
        except:
            routesRoot = ['10.0.0.0/8']

        connectToRootNS(network, switch, rootIp, routesRoot)

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


def run(topologyTemplate, xterm='disable'):
    """Main function to run virtul topology
    topologyTemplate: template for topology to run
    xterm: param for run all hosts with xterm, loaded from GUI not from template"""

    try:
        networkSetup, networkTemplate = loadNetworkSetup(topologyTemplate)

        # if 'networkSetup' is not defined in template
        if networkSetup is None:
            networkSetup = {}
        if xterm == 'enable':
            networkSetup['xterm'] = True
        else:
            networkSetup['xterm'] = False

        net = virtualNetwork(networkSetup, networkTemplate)  # argv[1:] only params without script name
        sshd(net, networkSetup)
    except Exception as e:
        print("Something went wrong " + str(e))


if __name__ == '__main__':

    try:
        lg.setLogLevel('info')
        run(sys.argv[1], sys.argv[2])
    except Exception as e:
        print("Something went wrong " + str(e))
