from sdn_controllers.sdnController import SDNController

import config
import os
import http.client
import json


class Ryu(SDNController):
    """Ryu SDN Controller"""

    def __init__(self):
        self.ryuSDNControllerPath = '/home/user/PycharmProjects/SDNControllers/ryu'

    def run(self, SDNControllerSetup):
        """Run SDN controller in new terminal window"""

        try:
            runOptions = ''
            for o in SDNControllerSetup:
                runOptions += ' ' + o

            os.system(
                'gnome-terminal -- bash -c "cd {} && /bin/ryu-manager{} && bash"'.format(self.ryuSDNControllerPath,
                                                                                 runOptions))
        except Exception as e:
            print("Something went wrong " + str(e))

    def isRunning(self):
        """Returns state of SDN Controller: True/False"""
        try:
            return True
        except Exception as e:
            print("Something went wrong " + str(e))
            return False

    def showSDNControllerGui(self):
        """Show SDN Controller GUI in web browser"""

        try:
            os.system('gnome-terminal -- bash -c "/bin/su user /usr/bin/firefox http://localhost:8080/"')
        except Exception as e:
            print("Something went wrong " + str(e))

    def addFlow(self, data, path='/stats/flowentry/add'):
        """Insert a static entry
            data: JSON string"""

        try:
            ret = self.restCall(path, data, 'POST')
            return ret[0] == 200
        except Exception as e:
            print("Something went wrong " + str(e))

    def deleteFlow(self, data, path='/stats/flowentry/delete'):
        """Delete a static entry
            data: JSON string"""

        try:
            ret = self.restCall(path, data, 'POST')
            return ret[0] == 200
        except Exception as e:
            print("Something went wrong " + str(e))

    def listFlowTable(self, device):
        """Get a list of all static entries
        device:
            switch_ID - static flows on a per-switch basis"""

        try:
            ret = self.restCall('/stats/flow/{}'.format(device), {}, 'GET')
            return json.loads(ret[2])
        except Exception as e:
            print("Something went wrong " + str(e))

    def clearFlowTable(self, device):
        """Clear a table of all static entries
        device:
            switch_ID - static flows on a per-switch basis"""

        try:
            ret = self.restCall('/stats/flowentry/clear/{}'.format(device), {}, 'DELETE')
            return ret[0] == 200
        except Exception as e:
            print("Something went wrong " + str(e))

    def restCall(self, path, data, action):
        """Rest Call for SDN controller
            path: REST CALL URL
            data: JSON string
            action: GET|POST|DELETE"""

        try:
            headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json',
            }
            body = json.dumps(data)
            conn = http.client.HTTPConnection('localhost', 8080)
            conn.request(action, path, body, headers)
            response = conn.getresponse()
            ret = (response.status, response.reason, response.read())
            conn.close()
            return ret
        except Exception as e:
            print("Something went wrong " + str(e))


if __name__ == "__main__":
    pusher = Ryu()
    print(pusher.listFlowTable('1'))
    print(pusher.clearFlowTable('1'))
    print(pusher.listFlowTable('1'))

    data = {
        'dpid': 1,
        'actions': [
            {
                'type': 'OUTPUT',
                'port': 2
            }
        ],
        'match': {
            'dl_dst': '01:80:c2:00:00:0e',
            'dl_type': 35020
        },
        'table_id': 0
    }

    print(pusher.deleteFlow(data))
    print(pusher.listFlowTable('1'))
    print(pusher.addFlow(data))
    print(pusher.listFlowTable('1'))
