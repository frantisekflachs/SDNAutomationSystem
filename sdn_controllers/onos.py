import http
import json
import shutil
from base64 import b64encode

from sdn_controllers.sdnController import SDNController
import os


class Onos(SDNController):
    """ONOS SDN Controller"""

    def __init__(self):
        self.onosSDNControllerPath = '/home/user/PycharmProjects/SDNControllers/onos'

    def run(self, SDNControllerSetup):
        """Run SDN controller in new terminal window"""

        try:
            # copy user defined configuration
            ret = self.__copyConfig(SDNControllerSetup)
            if ret:
                print("User defined config was applied.")
                # run SDN Controller with user defined config
                os.system(
                    'gnome-terminal -- bash -c "export TERM=xterm-color && {}/bin/onos-service start && bash"'.format(
                        self.onosSDNControllerPath))
            else:
                ret = self.__copyConfig('onos_default_config')
                if ret:
                    print("User defined config failed, starting with default config.")
                    # run SDN Controller with default config
                    os.system(
                        'gnome-terminal -- bash -c "export TERM=xterm-color && {}/bin/onos-service start && bash"'.format(
                            self.onosSDNControllerPath))
                else:
                    print("Starting failed.")
        except Exception as e:
            print("Something went wrong " + str(e))

    def __copyConfig(self, SDNControllerSetup):
        """Copy custom configuration before starting SDN controller"""

        try:
            shutil.copy2('/home/user/PycharmProjects/SDNAutomationSystem/sdn_controllers/startup_config/onos/{}'.format(
                SDNControllerSetup),
                '/home/user/PycharmProjects/SDNControllers/onos/apache-karaf-3.0.8/etc/org.apache.karaf.features.cfg')
        except Exception as e:
            print("Something went wrong " + str(e))
            return False
        else:
            return True

    def isRunning(self):
        """Returns state of SDN Controller: True/False"""

        try:
            ret = self.systemInfo()
            if ret is not None:
                return True
            else:
                return False
        except Exception as e:
            print("Something went wrong " + str(e))
            return False

    def systemInfo(self):
        """Returns system informations"""

        try:
            ret = self.restCall('/onos/v1/system', {}, 'GET')
            return json.loads(ret[2])
        except Exception as e:
            print("Something went wrong " + str(e))

    def listInstalledApplications(self, appName):
        """Returns list of installed applications
        app: all/app_name"""

        try:
            if appName is "all":
                ret = self.restCall('/onos/v1/applications', {}, 'GET')
                return json.loads(ret[2])
            else:
                ret = self.restCall('/onos/v1/applications/{}'.format(appName), {}, 'GET')
                return json.loads(ret[2])
        except Exception as e:
            print("Something went wrong " + str(e))

    def applicationState(self, appName):
        """Returns application state: ACTIVE/INSTALLED"""

        try:
            ret = self.listInstalledApplications(appName)
            return ret['state']
        except Exception as e:
            print("Something went wrong " + str(e))

    def activateApplication(self, appName):
        """Activate application by name
        app: app_name"""

        try:
            ret = self.restCall('/onos/v1/applications/{}/active'.format(appName), {}, 'POST')
            return ret
        except Exception as e:
            print("Something went wrong " + str(e))

    def deactivateApplication(self, appName):
        """Deactivate application by name
        app: app_name"""

        try:
            ret = self.restCall('/onos/v1/applications/{}/active'.format(appName), {}, 'DELETE')
            return ret
        except Exception as e:
            print("Something went wrong " + str(e))

    def showSDNControllerGui(self):
        """Show SDN Controller GUI in web browser"""

        try:
            os.system(
                'gnome-terminal -- bash -c "/bin/su user /usr/bin/firefox http://127.0.0.1:8181/onos/ui/login.html"')
        except Exception as e:
            print("Something went wrong " + str(e))

    def addFlow(self, data, path='/onos/v1/flows?appId=666'):
        """Insert a static entry
            data: JSON string"""

        try:
            ret = self.restCall(path, data, 'POST')
            return ret[0] == 200
        except Exception as e:
            print("Something went wrong " + str(e))

    def deleteFlow(self, data, path='http://localhost:8181/onos/v1/flows/of:0000000000000001/1'):
        """Delete a static entry
            data: JSON string"""

        try:
            if data:
                deviceId = data['deviceId']
                flowId = data['flowId']
                path = 'http://localhost:8181/onos/v1/flows/{}/{}'.format(deviceId, flowId)
            ret = self.restCall(path, {}, 'DELETE')
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
    #
    # print(pusher.listFlowTable('of:0000000000000001'))
    # print(pusher.addFlow(flow2))
    # print(pusher.addFlow(flow3))
    # print(pusher.addFlow(flow4))
    # print(pusher.listFlowTable('of:0000000000000001'))
    #
    # print(pusher.deleteFlow(flow1))
    # print(pusher.deleteFlow(path='http://localhost:8181/onos/v1/flows/of:0000000000000001/52917299094404191'))
    #
    # print(pusher.listFlowTable('of:0000000000000001'))
    #
    # print(pusher.clearFlowTable('of:0000000000000001'))
    # print(pusher.listFlowTable('of:0000000000000001'))

    # print(pusher.listInstalledApplications('org.onosproject.fwd'))
    # print(pusher.activateApplication('org.onosproject.fwd'))
    # print(pusher.listInstalledApplications('org.onosproject.fwd'))
    # print(pusher.deactivateApplication('org.onosproject.fwd'))
    # print(pusher.applicationState('org.onosproject.fwd'))
    # print(pusher.listInstalledApplications('org.onosproject.fwd'))
    # print(pusher.activateApplication('org.onosproject.fwd'))
    # print(pusher.listInstalledApplications('org.onosproject.fwd'))

    # print(pusher.applicationState('org.onosproject.fwd'))
    print(pusher.listFlowTable('of:0000000000000001'))

    # flows = {'flows': [
    #     {'id': '281475012051420', 'tableId': '0', 'appId': 'org.onosproject.core', 'groupId': 0, 'priority': 5,
    #      'timeout': 0, 'isPermanent': true, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 233,
    #      'packets': 11, 'bytes': 1248, 'liveType': 'UNKNOWN', 'lastSeen': 1588620490420,
    #      'treatment': {'instructions': [{'type': 'OUTPUT', 'port': 'CONTROLLER'}], 'clearDeferred': true,
    #                    'deferred': []}, 'selector': {'criteria': [{'type': 'ETH_TYPE', 'ethType': '0x800'}]}},
    #
    #     {'id': '281477466379610', 'tableId': '0', 'appId': 'org.onosproject.core', 'groupId': 0, 'priority': 40000,
    #      'timeout': 0, 'isPermanent': true, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 300,
    #      'packets': 0, 'bytes': 0, 'liveType': 'UNKNOWN', 'lastSeen': 1588620490420,
    #      'treatment': {'instructions': [{'type': 'OUTPUT', 'port': 'CONTROLLER'}], 'clearDeferred': true,
    #                    'deferred': []}, 'selector': {'criteria': [{'type': 'ETH_TYPE', 'ethType': '0x88cc'}]}},
    #
    #
    #
    #     {'id': '281477029321583', 'tableId': '0', 'appId': 'org.onosproject.core', 'groupId': 0, 'priority': 40000,
    #      'timeout': 0, 'isPermanent': true, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 300,
    #      'packets': 0, 'bytes': 0, 'liveType': 'UNKNOWN', 'lastSeen': 1588620490420,
    #      'treatment': {'instructions': [{'type': 'OUTPUT', 'port': 'CONTROLLER'}], 'clearDeferred': true,
    #                    'deferred': []}, 'selector': {'criteria': [{'type': 'ETH_TYPE', 'ethType': '0x8942'}]}},
    #
    #     {'id': '281478909873038', 'tableId': '0', 'appId': 'org.onosproject.core', 'groupId': 0, 'priority': 40000,
    #      'timeout': 0, 'isPermanent': true, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 300,
    #      'packets': 537, 'bytes': 22554, 'liveType': 'UNKNOWN', 'lastSeen': 1588620490420,
    #      'treatment': {'instructions': [{'type': 'OUTPUT', 'port': 'CONTROLLER'}], 'clearDeferred': true,
    #                    'deferred': []}, 'selector': {'criteria': [{'type': 'ETH_TYPE', 'ethType': '0x806'}]}}]}
    #
    # f={'flows': [
    # {'id': '10414574617121881', 'tableId': '0', 'appId': 'org.onosproject.fwd', 'groupId': 0, 'priority': 10,
    #  'timeout': 10, 'isPermanent': false, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 0,
    #  'packets': 1, 'bytes': 98, 'liveType': 'UNKNOWN', 'lastSeen': 1588620490420,
    #  'treatment': {'instructions': [{'type': 'OUTPUT', 'port': '2'}], 'deferred': []}, 'selector': {
    #     'criteria': [{'type': 'IN_PORT', 'port': 1}, {'type': 'ETH_DST', 'mac': '96:54:62:B9:AF:CC'},
    #                  {'type': 'ETH_SRC', 'mac': 'FA:6C:81:42:CE:36'}]}},
    #
    # {'id': '10414575001262020', 'tableId': '0', 'appId': 'org.onosproject.fwd', 'groupId': 0, 'priority': 10,
    #  'timeout': 10, 'isPermanent': false, 'deviceId': 'of:0000000000000001', 'state': 'ADDED', 'life': 0,
    #  'packets': 1, 'bytes': 98, 'liveType': 'UNKNOWN', 'lastSeen': 1588620490420,
    #  'treatment': {'instructions': [{'type': 'OUTPUT', 'port': '1'}], 'deferred': []}, 'selector': {
    #     'criteria': [{'type': 'IN_PORT', 'port': 2}, {'type': 'ETH_DST', 'mac': 'FA:6C:81:42:CE:36'},
    #                  {'type': 'ETH_SRC', 'mac': '96:54:62:B9:AF:CC'}]}}
    # ]}

    print(pusher.clearFlowTable('of:0000000000000001'))

