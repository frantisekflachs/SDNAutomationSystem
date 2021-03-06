"""Configuration file for the SDN Automation System"""
from network_templates.network1 import Network1
from network_templates.network2 import Network2
from network_templates.network3 import Network3
from network_templates.network4 import Network4
from sdn_controllers.opendaylight import Opendaylight
from sdn_controllers.floodlight import Floodlight
from sdn_controllers.onos import Onos
from sdn_controllers.pox import Pox
from sdn_controllers.ryu import Ryu

# log setup
logsPath = '/home/user/PycharmProjects/SDNAutomationSystem/Logs'

# help setup
readme = '/home/user/PycharmProjects/SDNAutomationSystem/README.md'

# self script for exercises
pathExercises = '/home/user/PycharmProjects/SDNAutomationSystem/exercises'

# SDN Controllers setup
implementedSDNControllers = {
    'Floodlight': Floodlight(),
    'Onos': Onos(),
    'Opendaylight': Opendaylight(),
    'Pox': Pox(),
    'Ryu': Ryu()
}

implementedSDNControllersNames = list(implementedSDNControllers.keys())
implementedSDNControllersClasses = list(implementedSDNControllers.values())

# Topology Templates setup
topologyTemplatesPath = '/home/user/PycharmProjects/SDNAutomationSystem/network_templates'
topologyTemplatesConfigPath = '/home/user/PycharmProjects/SDNAutomationSystem/topology_templates'

implementedVirtualNetworks = {
    'network1': Network1(),
    'network2': Network2(),
    'network3': Network3(),
    'network4': Network4(),
}
