import inspect
import os
import sys

from sdn_controllers.floodlight import Floodlight

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


def floodlight():
    pusher = Floodlight()
    print(pusher.isRunning())

    flow1 = {
        'switch': "00:00:00:00:00:00:00:01",
        "name": "flow_1",
        "cookie": "0",
        "priority": "32768",
        "in_port": "1",
        "active": "true",
        "actions": "output=flood"
    }

    flow2 = {
        'switch': "00:00:00:00:00:00:00:01",
        "name": "flow_2",
        "cookie": "0",
        "priority": "32768",
        "in_port": "2",
        "active": "true",
        "actions": "output=flood"
    }

    flow3 = {
        'switch': "00:00:00:00:00:00:00:02",
        "name": "flow_3",
        "cookie": "0",
        "priority": "32768",
        "in_port": "1",
        "active": "true",
        "actions": "output=flood"
    }

    flow4 = {
        'switch': "00:00:00:00:00:00:00:02",
        "name": "flow_4",
        "cookie": "0",
        "priority": "32768",
        "in_port": "2",
        "active": "true",
        "actions": "output=flood"
    }

    flow5 = {
        'switch': "00:00:00:00:00:00:00:01",
        "name": "flow_5",
        "cookie": "0",
        "priority": "32768",
        "in_port": "3",
        "active": "true",
        "actions": "output=flood"
    }

    flow6 = {
        'switch': "00:00:00:00:00:00:00:02",
        "name": "flow_6",
        "cookie": "0",
        "priority": "32768",
        "in_port": "3",
        "active": "true",
        "actions": "output=flood"
    }

    print(pusher.listFlowTable('all'))

    print(pusher.addFlow(flow1))
    print(pusher.addFlow(flow2))
    print(pusher.addFlow(flow3))
    print(pusher.addFlow(flow4))
    print(pusher.addFlow(flow5))
    print(pusher.addFlow(flow6))

    print(pusher.listFlowTable('all'))


if __name__ == '__main__':
    floodlight()
