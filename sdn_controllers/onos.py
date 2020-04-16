import http
import json
from base64 import b64encode

from sdn_controllers.sdnController import SDNController
import config

import os


class Onos(SDNController):
    """ONOS SDN Controller"""

    def run(self, SDNControllerSetup):
        """Run SDN controller in new terminal window"""

        try:
            os.system(
                'gnome-terminal -- bash -c "export TERM=xterm-color && {}/onos/bin/onos-service start && bash"'.format(
                    config.SDNControllersPath))
        except Exception as e:
            print("Something went wrong " + str(e))

    def showSDNControllerGui(self):
        """Show SDN Controller GUI in web browser"""

        try:
            os.system(
                'gnome-terminal -- bash -c "/bin/su user /usr/bin/firefox http://127.0.0.1:8181/onos/ui/login.html"')
        except Exception as e:
            print("Something went wrong " + str(e))

    def addFlow(self, data):
        """Insert a static entry
            data: JSON string"""

        try:
            ret = self.restCall('/onos/v1/flows?appId=666', data, 'POST')
            return ret[0] == 200
        except Exception as e:
            print("Something went wrong " + str(e))

    def deleteFlow(self, data):
        """Delete a static entry
            data: JSON string"""

        try:
            deviceId = data['deviceId']
            flowId = data['flowId']
            ret = self.restCall('http://localhost:8181/onos/v1/flows/{}/{}'.format(deviceId, flowId), {}, 'DELETE')
            return ret[0] == 204
        except Exception as e:
            print("Something went wrong " + str(e))

    def listFlowTable(self, device):
        """Get a list of all static entries
        device:
            switch_ID - static flows on a per-switch basis"""

        try:
            ret = self.restCall('/onos/v1/flows/{}'.format(device), {}, 'GET')
            return json.loads(ret[2])
        except Exception as e:
            print("Something went wrong " + str(e))

    def clearFlowTable(self, device):
        """Clear a table of all static entries
        device:
            switch_ID - static flows on a per-switch basis"""

        try:
            ret = self.listFlowTable(device)
            flowsID = []
            stat = True
            for flows in ret.values():
                for flow in flows:
                    flowsID.append(flow['id'])
            for fId in flowsID:
                data = {
                    'deviceId': device,
                    'flowId': fId
                }
                ret2 = self.deleteFlow(data)
                if not ret2:
                    stat = False
                    print('Problem with deleting flowId: ' + fId)
            return stat
        except Exception as e:
            print("Something went wrong " + str(e))

    def restCall(self, path, data, action):
        """Rest Call for SDN controller
            path: REST CALL URL
            data: JSON string
            action: GET|POST|DELETE"""

        try:
            userAndPass = b64encode(b"onos:rocks").decode("ascii")
            headers = {
                'Accept': 'application/json',
                'Authorization': 'Basic {}'.format(userAndPass),
            }
            body = json.dumps(data)
            conn = http.client.HTTPConnection('localhost', 8181)
            conn.request(action, path, body, headers)
            response = conn.getresponse()
            ret = (response.status, response.reason, response.read())
            conn.close()
            return ret
        except Exception as e:
            print("Something went wrong " + str(e))


if __name__ == "__main__":
    pusher = Onos()

    flow1 = {
        'deviceId': 'of:0000000000000001',
        'flowId': '52917299094404191'
    }
    flow2 = {
        "flows": [
            {
                "priority": 10000,
                "timeout": 0,
                "isPermanent": "true",
                "deviceId": "of:0000000000000001",
                "treatment": {
                    "instructions": [
                        {
                            "type": "OUTPUT",
                            "port": "CONTROLLER"
                        }
                    ]
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
    flow3 = {
        "flows": [
            {
                "priority": 20000,
                "timeout": 0,
                "isPermanent": "true",
                "deviceId": "of:0000000000000001",
                "treatment": {
                    "instructions": [
                        {
                            "type": "OUTPUT",
                            "port": "CONTROLLER"
                        }
                    ]
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
    flow4 = {
        "flows": [
            {
                "priority": 30000,
                "timeout": 0,
                "isPermanent": "true",
                "deviceId": "of:0000000000000001",
                "treatment": {
                    "instructions": [
                        {
                            "type": "OUTPUT",
                            "port": "CONTROLLER"
                        }
                    ]
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
    print(pusher.addFlow(flow2))
    print(pusher.addFlow(flow3))
    print(pusher.addFlow(flow4))
    print(pusher.listFlowTable('of:0000000000000001'))
    print(pusher.deleteFlow(flow1))
    print(pusher.listFlowTable('of:0000000000000001'))

    print(pusher.clearFlowTable('of:0000000000000001'))
    print(pusher.listFlowTable('of:0000000000000001'))
