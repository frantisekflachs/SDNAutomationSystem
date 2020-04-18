import http
import json
import os
from base64 import b64encode

from sdn_controllers.sdnController import SDNController
import config


class Opendaylight(SDNController):
    """OpenDaylight SDN Controller"""

    def __init__(self):
        self.opendaylightSDNControllerPath = '/home/user/PycharmProjects/SDNControllers/opendaylight'

    def run(self, SDNControllerSetup):
        """Run SDN controller in new terminal window"""

        try:
            os.system('gnome-terminal -- bash -c "export TERM=xterm-color && {}/bin/karaf && bash"'.format(
                    self.opendaylightSDNControllerPath))
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
        """Show SDN Controller GUI and OpenFlow App GUI in web browser"""

        try:
            os.system('gnome-terminal -- bash -c "cd /home/user/PycharmProjects/SDNControllers/OpenDaylight-Openflow-App-master && grunt && bash"')
            os.system('gnome-terminal -- bash -c "/bin/su user /usr/bin/firefox http://localhost:8181/index.html http://localhost:9000"')
        except Exception as e:
            print("Something went wrong " + str(e))

    def addFlow(self, data, path='/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/0/flow/666'):
        """Insert a static entry
            data: JSON string"""

        try:
            ret = self.restCall(path, data, 'PUT')
            return ret[0] == 200 or ret[0] == 201
        except Exception as e:
            print("Something went wrong " + str(e))

    def deleteFlow(self, data, path='/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/0/flow/1'):
        """Delete a static entry
            data: JSON string"""

        try:
            ret = self.restCall(path, data, 'DELETE')
            return ret[0] == 200
        except Exception as e:
            print("Something went wrong " + str(e))

    def listFlowTable(self, device):
        """Get a list of all static entries
        device:
            switch_ID - static flows on a per-switch basis"""

        try:
            ret = self.restCall('/restconf/operational/opendaylight-inventory:nodes/node/{}'.format(device), {}, 'GET')
            return json.loads(ret[2])
            # return ret
        except Exception as e:
            print("Something went wrong " + str(e))

    def clearFlowTable(self, device):
        """Clear a table of all static entries
        device:
            switch_ID - static flows on a per-switch basis"""

        idsToDelete = {}
        data = self.listFlowTable('openflow:1')
        data1 = data['node'][0]['flow-node-inventory:table']

        # parse data from listFlowTable per device
        for flows in data1:
            tmp = flows['opendaylight-flow-table-statistics:flow-table-statistics']
            if tmp['active-flows'] is not 0:
                tableIdWithFlows = flows['id']
                if flows['id'] is tableIdWithFlows:
                    flws = flows['flow']
                    for f in flws:
                        print(f['id'])
                        if tableIdWithFlows not in idsToDelete.keys():
                            values = []
                            values.append(f['id'])
                            idsToDelete[tableIdWithFlows] = values
                        else:
                            values = idsToDelete[tableIdWithFlows]
                            values.append(f['id'])
                            idsToDelete[tableIdWithFlows] = values

        # delete all found flows in all found tables with flows
        for tableId, flowIds in idsToDelete.items():
            for flowId in flowIds:
                data = {"id": flowId}
                ret = self.deleteFlow(data, path='/restconf/config/opendaylight-inventory:nodes/node/{}/table/{}/flow/{}'.format(device, tableId, flowId))
                print(ret)

    def restCall(self, path, data, action):
        """Rest Call for SDN controller
            path: REST CALL URL
            data: JSON string
            action: GET|POST|DELETE"""

        try:
            userAndPass = b64encode(b"admin:admin").decode("ascii")
            headers = {
                'Accept': 'application/json',
                'Content-type': 'application/json',
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
    pusher = Opendaylight()
    # {"flow":[{"table_id":"0","id":"20","priority":"20","flow-name":"test","instructions":{"instruction":[{"order":0,"apply-actions":{"action":[{"order":0,"output-action":{"output-node-connector":"CONTROLLER"}},{"order":1,"output-action":{"output-node-connector":"2"}}]}}]},"hard-timeout":"0","idle-timeout":"0","installHw":"false","strict":"false"}]}
    # http://localhost:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0

    print(pusher.listFlowTable('openflow:1'))
    #
    # flow1 = {
    #     "id": 0,
    #     "flow": [
    #         {
    #             "id": "test-flow",
    #             "cookie_mask": 0,
    #             "priority": 5,
    #             "table_id": 0,
    #             "cookie": 3098476543630900000,
    #         }
    #     ]
    # }

    # flow2 = {"flow":[{"table_id":"0","id":"20","priority":"20","flow-name":"test","instructions":{"instruction":[{"order":0,"apply-actions":{"action":[{"order":0,"output-action":{"output-node-connector":"CONTROLLER"}},{"order":1,"output-action":{"output-node-connector":"2"}}]}}]},"hard-timeout":"0","idle-timeout":"0","installHw":"false","strict":"false"}]}
    #
    # flow3 = {"flow":[{"table_id":"0","id":"1","priority":"7","hard-timeout":"0","idle-timeout":"0","installHw":"false","strict":"false"}]}
    # print(pusher.addFlow(flow3, path='/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/0/flow/1'))
    #
    # flow4 = {"id":"666"}
    # print(pusher.deleteFlow(flow4, path='/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/0/flow/666'))

    print(pusher.clearFlowTable('openflow:1'))