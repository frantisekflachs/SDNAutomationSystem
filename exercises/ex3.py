import inspect
import os
import sys

from sdn_controllers.floodlight import Floodlight
from sdn_controllers.onos import Onos

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


def floodlight():
    pusher = Floodlight()
    print(pusher.isRunning())

    flow1 = {
        'switch': "00:00:00:00:00:00:00:01",
        "name": "flow_mod_1",
        "cookie": "0",
        "priority": "32768",
        "in_port": "1",
        "active": "true",
        "actions": "output=flood"
    }

    flow2 = {
        'switch': "00:00:00:00:00:00:00:01",
        "name": "flow_mod_2",
        "cookie": "0",
        "priority": "32768",
        "in_port": "2",
        "active": "true",
        "actions": "output=flood"
    }

    flow3 = {
        'switch': "00:00:00:00:00:00:00:02",
        "name": "flow_mod_3",
        "cookie": "0",
        "priority": "32768",
        "in_port": "1",
        "active": "true",
        "actions": "output=flood"
    }

    flow4 = {
        'switch': "00:00:00:00:00:00:00:02",
        "name": "flow_mod_4",
        "cookie": "0",
        "priority": "32768",
        "in_port": "2",
        "active": "true",
        "actions": "output=flood"
    }

    flow5 = {
        'switch': "00:00:00:00:00:00:00:01",
        "name": "flow_mod_5",
        "cookie": "0",
        "priority": "32768",
        "in_port": "3",
        "active": "true",
        "actions": "output=flood"
    }

    flow6 = {
        'switch': "00:00:00:00:00:00:00:02",
        "name": "flow_mod_6",
        "cookie": "0",
        "priority": "32768",
        "in_port": "3",
        "active": "true",
        "actions": "output=flood"
    }

    pusher.clearFlowTable('all')
    print(pusher.listFlowTable('all'))

    print(pusher.addFlow(flow1))
    print(pusher.addFlow(flow2))
    print(pusher.addFlow(flow3))
    print(pusher.addFlow(flow4))
    print(pusher.addFlow(flow5))
    print(pusher.addFlow(flow6))

    print(pusher.listFlowTable('all'))


def onos():
    pusher = Onos()

    flow1 = {"flows": [{
        'tableId': '0',
        'groupId': 0,
        'priority': 10,
        'timeout': 10,
        'isPermanent': False,
        'deviceId': 'of:0000000000000001',
        'state': 'ADDED',
        'treatment':
            {
                'instructions':
                    [
                        {
                            'type': 'OUTPUT',
                            'port': '3'
                        }
                    ],
                'deferred': []
            },
        'selector':
            {
                'criteria':
                    [
                        {
                            'type': 'IN_PORT',
                            'port': 1
                        },
                        {
                            'type': 'ETH_DST',
                            'mac': 'F6:EC:13:E1:AA:B6'
                        },
                        {
                            'type': 'ETH_SRC',
                            'mac': '16:9C:A6:E9:B1:8B'
                        }
                    ]
            }
    }
    ]
    }
    flow2 = {
        'id': '281475012051420',
        'tableId': '0',
        'appId': 'org.onosproject.core',
        'groupId': 0,
        'priority': 5,
        'timeout': 0,
        'isPermanent': True,
        'deviceId': 'of:0000000000000001',
        'state': 'ADDED',
        'life': 475,
        'packets': 38,
        'bytes': 3694,
        'liveType': 'UNKNOWN',
        'lastSeen': 1588463159651,
        'treatment':
            {
                'instructions':
                    [
                        {
                            'type': 'OUTPUT',
                            'port': 'CONTROLLER'
                        }
                    ],
                'clearDeferred': True,
                'deferred': []
            },
        'selector':
            {
                'criteria':
                    [
                        {
                            'type': 'ETH_TYPE',
                            'ethType': '0x800'
                        }
                    ]
            }
    }
    flow3 = {
        'id': '10414574277227041',
        'tableId': '0',
        'appId': 'org.onosproject.fwd',
        'groupId': 0,
        'priority': 10,
        'timeout': 10,
        'isPermanent': False,
        'deviceId': 'of:0000000000000001',
        'state': 'ADDED',
        'life': 3,
        'packets': 1,
        'bytes': 98,
        'liveType': 'UNKNOWN',
        'lastSeen': 1588463159651,
        'treatment':
            {
                'instructions':
                    [
                        {
                            'type': 'OUTPUT',
                            'port': '2'
                        }
                    ],
                'deferred': []
            },
        'selector':
            {
                'criteria':
                    [
                        {
                            'type': 'IN_PORT',
                            'port': 3
                        },
                        {
                            'type': 'ETH_DST',
                            'mac': '32:D2:EB:A8:DB:9E'
                        },
                        {
                            'type': 'ETH_SRC',
                            'mac': '86:BC:58:3F:FE:E4'
                        }
                    ]
            }
    }
    flow4 = {
        'id': '10414578050956862',
        'tableId': '0',
        'appId': 'org.onosproject.fwd',
        'groupId': 0,
        'priority': 10,
        'timeout': 10,
        'isPermanent': False,
        'deviceId': 'of:0000000000000001',
        'state': 'ADDED',
        'life': 3,
        'packets': 1,
        'bytes': 98,
        'liveType': 'UNKNOWN',
        'lastSeen': 1588463159651,
        'treatment':
            {
                'instructions':
                    [
                        {
                            'type': 'OUTPUT',
                            'port': '1'
                        }
                    ],
                'deferred': []
            },
        'selector':
            {
                'criteria':
                    [
                        {
                            'type': 'IN_PORT',
                            'port': 3
                        },
                        {
                            'type': 'ETH_DST',
                            'mac': '16:9C:A6:E9:B1:8B'
                        },
                        {
                            'type': 'ETH_SRC',
                            'mac': 'F6:EC:13:E1:AA:B6'
                        }
                    ]
            }
    }
    flow5 = {
        'id': '10414574716952738',
        'tableId': '0',
        'appId': 'org.onosproject.fwd',
        'groupId': 0,
        'priority': 10,
        'timeout': 10,
        'isPermanent': False,
        'deviceId': 'of:0000000000000001',
        'state': 'ADDED',
        'life': 3,
        'packets': 1,
        'bytes': 98,
        'liveType': 'UNKNOWN',
        'lastSeen': 1588463159651,
        'treatment':
            {
                'instructions':
                    [
                        {
                            'type': 'OUTPUT',
                            'port': '3'
                        }
                    ],
                'deferred': []
            },
        'selector':
            {
                'criteria':
                    [
                        {
                            'type': 'IN_PORT',
                            'port': 2
                        },
                        {
                            'type': 'ETH_DST',
                            'mac': '86:BC:58:3F:FE:E4'
                        },
                        {
                            'type': 'ETH_SRC',
                            'mac': '32:D2:EB:A8:DB:9E'
                        }
                    ]
            }
    }
    flow6 = {
        'id': '10414576233225243',
        'tableId': '0',
        'appId': 'org.onosproject.fwd',
        'groupId': 0,
        'priority': 10,
        'timeout': 10,
        'isPermanent': False,
        'deviceId': 'of:0000000000000001',
        'state': 'ADDED',
        'life': 3,
        'packets': 1,
        'bytes': 98,
        'liveType': 'UNKNOWN',
        'lastSeen': 1588463159651,
        'treatment':
            {
                'instructions':
                    [
                        {
                            'type': 'OUTPUT',
                            'port': '3'
                        }
                    ],
                'deferred': []
            },
        'selector':
            {
                'criteria':
                    [
                        {
                            'type': 'IN_PORT',
                            'port': 2
                        },
                        {
                            'type': 'ETH_DST',
                            'mac': 'F6:EC:13:E1:AA:B6'
                        },
                        {
                            'type': 'ETH_SRC',
                            'mac': '32:D2:EB:A8:DB:9E'
                        }
                    ]
            }
    }
    flow7 = {
        'id': '10414575571877435',
        'tableId': '0',
        'appId': 'org.onosproject.fwd',
        'groupId': 0,
        'priority': 10,
        'timeout': 10,
        'isPermanent': False,
        'deviceId': 'of:0000000000000001',
        'state': 'ADDED',
        'life': 3,
        'packets': 1,
        'bytes': 98,
        'liveType': 'UNKNOWN',
        'lastSeen': 1588463159651,
        'treatment':
            {
                'instructions':
                    [
                        {
                            'type': 'OUTPUT',
                            'port': '2'
                        }
                    ],
                'deferred': []
            },
        'selector':
            {
                'criteria':
                    [
                        {
                            'type': 'IN_PORT',
                            'port': 3
                        },
                        {
                            'type': 'ETH_DST',
                            'mac': '32:D2:EB:A8:DB:9E'
                        },
                        {
                            'type': 'ETH_SRC',
                            'mac': 'F6:EC:13:E1:AA:B6'
                        }
                    ]
            }
    }

    flow8 = {'id': '281477029321583', 'tableId': '0', 'appId': 'org.onosproject.core', 'groupId': 0, 'priority': 40000,
             'timeout': 0, 'isPermanent': True, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 475,
             'packets': 153, 'bytes': 19890, 'liveType': 'UNKNOWN', 'lastSeen': 1588463159651,
             'treatment': {'instructions': [{'type': 'OUTPUT', 'port': 'CONTROLLER'}], 'clearDeferred': True,
                           'deferred': []}, 'selector': {'criteria': [{'type': 'ETH_TYPE', 'ethType': '0x8942'}]}}
    flow9 = {'id': '281478909873038', 'tableId': '0', 'appId': 'org.onosproject.core', 'groupId': 0, 'priority': 40000,
             'timeout': 0, 'isPermanent': True, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 475,
             'packets': 1309, 'bytes': 54978, 'liveType': 'UNKNOWN', 'lastSeen': 1588463159651,
             'treatment': {'instructions': [{'type': 'OUTPUT', 'port': 'CONTROLLER'}], 'clearDeferred': True,
                           'deferred': []}, 'selector': {'criteria': [{'type': 'ETH_TYPE', 'ethType': '0x806'}]}}
    flow10 = {'id': '10414577924397128', 'tableId': '0', 'appId': 'org.onosproject.fwd', 'groupId': 0, 'priority': 10,
              'timeout': 10, 'isPermanent': False, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 3,
              'packets': 1, 'bytes': 98, 'liveType': 'UNKNOWN', 'lastSeen': 1588463159651,
              'treatment': {'instructions': [{'type': 'OUTPUT', 'port': '1'}], 'deferred': []}, 'selector': {
            'criteria': [{'type': 'IN_PORT', 'port': 3}, {'type': 'ETH_DST', 'mac': '16:9C:A6:E9:B1:8B'},
                         {'type': 'ETH_SRC', 'mac': '86:BC:58:3F:FE:E4'}]}}
    flow11 = {'id': '281477466379610', 'tableId': '0', 'appId': 'org.onosproject.core', 'groupId': 0, 'priority': 40000,
              'timeout': 0, 'isPermanent': True, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 475,
              'packets': 153, 'bytes': 19890, 'liveType': 'UNKNOWN', 'lastSeen': 1588463159651,
              'treatment': {'instructions': [{'type': 'OUTPUT', 'port': 'CONTROLLER'}], 'clearDeferred': True,
                            'deferred': []}, 'selector': {'criteria': [{'type': 'ETH_TYPE', 'ethType': '0x88cc'}]}}
    flow12 = {'id': '10414575920815862', 'tableId': '0', 'appId': 'org.onosproject.fwd', 'groupId': 0, 'priority': 10,
              'timeout': 10, 'isPermanent': False, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 3,
              'packets': 1, 'bytes': 98, 'liveType': 'UNKNOWN', 'lastSeen': 1588463159651,
              'treatment': {'instructions': [{'type': 'OUTPUT', 'port': '1'}], 'deferred': []}, 'selector': {
            'criteria': [{'type': 'IN_PORT', 'port': 2}, {'type': 'ETH_DST', 'mac': '16:9C:A6:E9:B1:8B'},
                         {'type': 'ETH_SRC', 'mac': '32:D2:EB:A8:DB:9E'}]}}
    flow13 = {'id': '10414575307656833', 'tableId': '0', 'appId': 'org.onosproject.fwd', 'groupId': 0, 'priority': 10,
              'timeout': 10, 'isPermanent': False, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 3,
              'packets': 1, 'bytes': 98, 'liveType': 'UNKNOWN', 'lastSeen': 1588463159651,
              'treatment': {'instructions': [{'type': 'OUTPUT', 'port': '2'}], 'deferred': []}, 'selector': {
            'criteria': [{'type': 'IN_PORT', 'port': 1}, {'type': 'ETH_DST', 'mac': '32:D2:EB:A8:DB:9E'},
                         {'type': 'ETH_SRC', 'mac': '16:9C:A6:E9:B1:8B'}]}}
    flow14 = {'id': '10414575984137880', 'tableId': '0', 'appId': 'org.onosproject.fwd', 'groupId': 0, 'priority': 10,
              'timeout': 10, 'isPermanent': False, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 3,
              'packets': 1, 'bytes': 98, 'liveType': 'UNKNOWN', 'lastSeen': 1588463159651,
              'treatment': {'instructions': [{'type': 'OUTPUT', 'port': '3'}], 'deferred': []}, 'selector': {
            'criteria': [{'type': 'IN_PORT', 'port': 1}, {'type': 'ETH_DST', 'mac': '86:BC:58:3F:FE:E4'},
                         {'type': 'ETH_SRC', 'mac': '16:9C:A6:E9:B1:8B'}]}}

    # print(pusher.isRunning())
    # print(pusher.listFlowTable('of:0000000000000001'))
    # print(pusher.clearFlowTable('of:0000000000000001'))

    # print(pusher.addFlow(flow1))
    # print(pusher.addFlow(flow2))
    # print(pusher.addFlow(flow3))
    # print(pusher.addFlow(flow4))
    # print(pusher.addFlow(flow5))
    # print(pusher.addFlow(flow6))
    # print(pusher.addFlow(flow7))
    # print(pusher.addFlow(flow8))
    # print(pusher.addFlow(flow9))
    # print(pusher.addFlow(flow10))
    # print(pusher.addFlow(flow11))
    # print(pusher.addFlow(flow12))
    # print(pusher.addFlow(flow13))
    # print(pusher.addFlow(flow14))

    # print(pusher.listFlowTable('of:0000000000000001'))

    # print(pusher.deactivateApplication('org.onosproject.fwd'))
    # print(pusher.applicationState('org.onosproject.fwd'))
    # print(pusher.listInstalledApplications('org.onosproject.fwd'))
    # print(pusher.activateApplication('org.onosproject.fwd'))

    # print(pusher.deactivateApplication('org.onosproject.fwd'))
    # print(pusher.applicationState('org.onosproject.fwd'))

    flows = {'flows': [
        {'id': '10414575112236379', 'tableId': '0', 'appId': 'org.onosproject.fwd', 'groupId': 0, 'priority': 10,
         'timeout': 10, 'isPermanent': False, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 3,
         'packets': 1, 'bytes': 98, 'liveType': 'UNKNOWN', 'lastSeen': 1588618380120,
         'treatment': {'instructions': [{'type': 'OUTPUT', 'port': '3'}], 'deferred': []}, 'selector': {
            'criteria': [{'type': 'IN_PORT', 'port': 1}, {'type': 'ETH_DST', 'mac': '22:F6:59:C8:57:5A'},
                         {'type': 'ETH_SRC', 'mac': 'BE:F1:54:85:EE:A4'}]}},
        {'id': '10414574614333950', 'tableId': '0', 'appId': 'org.onosproject.fwd', 'groupId': 0, 'priority': 10,
         'timeout': 10, 'isPermanent': False, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 3,
         'packets': 1, 'bytes': 98, 'liveType': 'UNKNOWN', 'lastSeen': 1588618380120,
         'treatment': {'instructions': [{'type': 'OUTPUT', 'port': '3'}], 'deferred': []}, 'selector': {
            'criteria': [{'type': 'IN_PORT', 'port': 2}, {'type': 'ETH_DST', 'mac': '22:F6:59:C8:57:5A'},
                         {'type': 'ETH_SRC', 'mac': '56:78:8E:9E:CA:90'}]}},
        {'id': '10414578344328580', 'tableId': '0', 'appId': 'org.onosproject.fwd', 'groupId': 0, 'priority': 10,
         'timeout': 10, 'isPermanent': False, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 3,
         'packets': 1, 'bytes': 98, 'liveType': 'UNKNOWN', 'lastSeen': 1588618380120,
         'treatment': {'instructions': [{'type': 'OUTPUT', 'port': '2'}], 'deferred': []}, 'selector': {
            'criteria': [{'type': 'IN_PORT', 'port': 3}, {'type': 'ETH_DST', 'mac': '56:78:8E:9E:CA:90'},
                         {'type': 'ETH_SRC', 'mac': '22:F6:59:C8:57:5A'}]}},
        {'id': '10414574747436280', 'tableId': '0', 'appId': 'org.onosproject.fwd', 'groupId': 0, 'priority': 10,
         'timeout': 10, 'isPermanent': False, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 3,
         'packets': 1, 'bytes': 98, 'liveType': 'UNKNOWN', 'lastSeen': 1588618380120,
         'treatment': {'instructions': [{'type': 'OUTPUT', 'port': '1'}], 'deferred': []}, 'selector': {
            'criteria': [{'type': 'IN_PORT', 'port': 3}, {'type': 'ETH_DST', 'mac': 'BE:F1:54:85:EE:A4'},
                         {'type': 'ETH_SRC', 'mac': '22:F6:59:C8:57:5A'}]}},
        {'id': '281475012051420', 'tableId': '0', 'appId': 'org.onosproject.core', 'groupId': 0, 'priority': 5,
         'timeout': 0, 'isPermanent': True, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 19,
         'packets': 11, 'bytes': 1078, 'liveType': 'UNKNOWN', 'lastSeen': 1588618380120,
         'treatment': {'instructions': [{'type': 'OUTPUT', 'port': 'CONTROLLER'}], 'clearDeferred': True,
                       'deferred': []}, 'selector': {'criteria': [{'type': 'ETH_TYPE', 'ethType': '0x800'}]}},
        {'id': '10414576625279615', 'tableId': '0', 'appId': 'org.onosproject.fwd', 'groupId': 0, 'priority': 10,
         'timeout': 10, 'isPermanent': False, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 3,
         'packets': 1, 'bytes': 98, 'liveType': 'UNKNOWN', 'lastSeen': 1588618380120,
         'treatment': {'instructions': [{'type': 'OUTPUT', 'port': '2'}], 'deferred': []}, 'selector': {
            'criteria': [{'type': 'IN_PORT', 'port': 3}, {'type': 'ETH_DST', 'mac': '56:78:8E:9E:CA:90'},
                         {'type': 'ETH_SRC', 'mac': '0A:F7:AE:C4:36:22'}]}},
        {'id': '10414575795366923', 'tableId': '0', 'appId': 'org.onosproject.fwd', 'groupId': 0, 'priority': 10,
         'timeout': 10, 'isPermanent': False, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 3,
         'packets': 1, 'bytes': 98, 'liveType': 'UNKNOWN', 'lastSeen': 1588618380120,
         'treatment': {'instructions': [{'type': 'OUTPUT', 'port': '3'}], 'deferred': []}, 'selector': {
            'criteria': [{'type': 'IN_PORT', 'port': 2}, {'type': 'ETH_DST', 'mac': '0A:F7:AE:C4:36:22'},
                         {'type': 'ETH_SRC', 'mac': '56:78:8E:9E:CA:90'}]}},
        {'id': '281477029321583', 'tableId': '0', 'appId': 'org.onosproject.core', 'groupId': 0,
         'priority': 40000, 'timeout': 0, 'isPermanent': True, 'deviceId': 'of:0000000000000001',
         'state': 'ADDED', 'life': 70, 'packets': 23, 'bytes': 2990, 'liveType': 'UNKNOWN',
         'lastSeen': 1588618380119,
         'treatment': {'instructions': [{'type': 'OUTPUT', 'port': 'CONTROLLER'}], 'clearDeferred': True,
                       'deferred': []}, 'selector': {'criteria': [{'type': 'ETH_TYPE', 'ethType': '0x8942'}]}},
        {'id': '281478909873038', 'tableId': '0', 'appId': 'org.onosproject.core', 'groupId': 0,
         'priority': 40000, 'timeout': 0, 'isPermanent': True, 'deviceId': 'of:0000000000000001',
         'state': 'ADDED', 'life': 70, 'packets': 268, 'bytes': 11256, 'liveType': 'UNKNOWN',
         'lastSeen': 1588618380120,
         'treatment': {'instructions': [{'type': 'OUTPUT', 'port': 'CONTROLLER'}], 'clearDeferred': True,
                       'deferred': []}, 'selector': {'criteria': [{'type': 'ETH_TYPE', 'ethType': '0x806'}]}},
        {'id': '10414577400092416', 'tableId': '0', 'appId': 'org.onosproject.fwd', 'groupId': 0, 'priority': 10,
         'timeout': 10, 'isPermanent': False, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 3,
         'packets': 1, 'bytes': 98, 'liveType': 'UNKNOWN', 'lastSeen': 1588618380120,
         'treatment': {'instructions': [{'type': 'OUTPUT', 'port': '1'}], 'deferred': []}, 'selector': {
            'criteria': [{'type': 'IN_PORT', 'port': 3}, {'type': 'ETH_DST', 'mac': 'BE:F1:54:85:EE:A4'},
                         {'type': 'ETH_SRC', 'mac': '0A:F7:AE:C4:36:22'}]}},
        {'id': '10414577971108610', 'tableId': '0', 'appId': 'org.onosproject.fwd', 'groupId': 0, 'priority': 10,
         'timeout': 10, 'isPermanent': False, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 3,
         'packets': 1, 'bytes': 98, 'liveType': 'UNKNOWN', 'lastSeen': 1588618380120,
         'treatment': {'instructions': [{'type': 'OUTPUT', 'port': '3'}], 'deferred': []}, 'selector': {
            'criteria': [{'type': 'IN_PORT', 'port': 1}, {'type': 'ETH_DST', 'mac': '0A:F7:AE:C4:36:22'},
                         {'type': 'ETH_SRC', 'mac': 'BE:F1:54:85:EE:A4'}]}},
        {'id': '10414577185152816', 'tableId': '0', 'appId': 'org.onosproject.fwd', 'groupId': 0, 'priority': 10,
         'timeout': 10, 'isPermanent': False, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 3,
         'packets': 1, 'bytes': 98, 'liveType': 'UNKNOWN', 'lastSeen': 1588618380120,
         'treatment': {'instructions': [{'type': 'OUTPUT', 'port': '1'}], 'deferred': []}, 'selector': {
            'criteria': [{'type': 'IN_PORT', 'port': 2}, {'type': 'ETH_DST', 'mac': 'BE:F1:54:85:EE:A4'},
                         {'type': 'ETH_SRC', 'mac': '56:78:8E:9E:CA:90'}]}},
        {'id': '281477466379610', 'tableId': '0', 'appId': 'org.onosproject.core', 'groupId': 0,
         'priority': 40000, 'timeout': 0, 'isPermanent': True, 'deviceId': 'of:0000000000000001',
         'state': 'ADDED', 'life': 70, 'packets': 23, 'bytes': 2990, 'liveType': 'UNKNOWN',
         'lastSeen': 1588618380120,
         'treatment': {'instructions': [{'type': 'OUTPUT', 'port': 'CONTROLLER'}], 'clearDeferred': True,
                       'deferred': []}, 'selector': {'criteria': [{'type': 'ETH_TYPE', 'ethType': '0x88cc'}]}},
        {'id': '10414574425174512', 'tableId': '0', 'appId': 'org.onosproject.fwd', 'groupId': 0, 'priority': 10,
         'timeout': 10, 'isPermanent': False, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 3,
         'packets': 0, 'bytes': 0, 'liveType': 'UNKNOWN', 'lastSeen': 1588618380120,
         'treatment': {'instructions': [{'type': 'OUTPUT', 'port': '2'}], 'deferred': []}, 'selector': {
            'criteria': [{'type': 'IN_PORT', 'port': 1}, {'type': 'ETH_DST', 'mac': '56:78:8E:9E:CA:90'},
                         {'type': 'ETH_SRC', 'mac': 'BE:F1:54:85:EE:A4'}]}}
    ]}

    # print(pusher.addFlow(flows))
    # print(pusher.listFlowTable('of:0000000000000001'))

    flowtest = {
        "flows": [
            {
                "priority": 5,
                "timeout": 0,
                "deviceId": "of:0000000000000001",
                "treatment": {
                    "instructions": [
                        {
                            "type": "OUTPUT",
                            "port": "CONTROLLER"
                        }
                    ],
                },
                "selector": {
                    "criteria": [
                        {
                            "type": "ETH_TYPE",
                            "ethType": "0x88cc"
                        }
                    ]
                }
            }
        ]
    }

    print(pusher.listFlowTable('of:0000000000000001'))
    print(pusher.addFlow(flowtest))
    print(pusher.listFlowTable('of:0000000000000001'))


if __name__ == '__main__':
    # floodlight()
    onos()
