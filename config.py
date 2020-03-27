"""Configuration file for the SDN Automation System"""

from sdn_controllers.opendaylight import Opendaylight
from sdn_controllers.floodlight import Floodlight
from sdn_controllers.onos import Onos
from sdn_controllers.pox import Pox
from sdn_controllers.ryu import Ryu

# log setup
logsPath = '/home/user/PycharmProjects/SDNAutomationSystem/Logs'

# SDN Controllers setup
SDNControllersPath = '/home/user/PycharmProjects/SDNControllers'
FloodlightSDNControllerPath = ''
OnosSDNControllerPath = ''
OpendaylightSDNControllerPath = ''
PoxSDNControllerPath = ''
RyuSDNControllerPath = ''

implementedSDNControllers = {
    'Floodlight': Floodlight,
    'Onos': Onos,
    'OpenDaylight': Opendaylight,
    'Pox': Pox,
    'Ryu': Ryu
}

implementedSDNControllersNames = list(implementedSDNControllers.keys())
implementedSDNControllersClasses = list(implementedSDNControllers.values())

# Topology Templates setup
topologyTemplatesPath = '/home/user/PycharmProjects/SDNAutomationSystem/network_templates'
topologyTemplatesConfigPath = '/home/user/PycharmProjects/SDNAutomationSystem/topology_templates_config'

# Topology templates
implementedTopologyTemplates = {
    'Topology 1 - OF 1.0, network1': 'topology1',
    'Topology 2 - OF 1.3, network1': 'topology2',
    'Topology 3 - OF 1.4, network2': 'topology3',
    'Topology 4 - OF 1.4, network3': 'topology3',
    'Topology 5 - OF 1.5, network3': 'topology3'
}