"""Configuration file for the SDN Automation System"""

from sdnControllers.opendaylight import Opendaylight
from sdnControllers.floodlight import Floodlight
from sdnControllers.onos import Onos
from sdnControllers.pox import Pox
from sdnControllers.ryu import Ryu

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

# Topology Templates setup
topologyTemplatesPath = '/home/user/PycharmProjects/SDNAutomationSystem/topologyTemplates'
topologyTemplatesConfigPath = '/home/user/PycharmProjects/SDNAutomationSystem/topologyTemplatesConfig'

# Topology templates
implementedTopologyTemplates = {
    'Topology 1 - 2 hosts, 1 switch': 'topology1',
    'Topology 2 - 4 hosts, 2 switches': 'topology2',
    'Topology 3 - 3 hosts, 1 switch': 'topology3'
}

# OpenFlow versions
implementedOFVersions = {
    'OF 1.0': '10',
    'OF 1.1': '11',
    'OF 1.2': '12',
    'OF 1.3': '13',
    'OF 1.4': '14',
    'OF 1.5': '15'
}

