from sdn_controllers.sdnController import SDNController

import subprocess
import os
import http.client
import json
import shutil


class Floodlight(SDNController):
    """Floodlight SDN Controller"""

    def __init__(self):
        self.floodlightSDNControllerPath = '/home/user/PycharmProjects/SDNControllers/floodlight'

    def run(self, SDNControllerSetup):
        """Run SDN controller in new terminal window"""

        try:
            # copy user defined configuration
            ret = self.__copyConfig(SDNControllerSetup)
            if ret:
                print("User defined config was applied.")
                # run SDN Controller with user defined config
                proc = subprocess.Popen(["gnome-terminal", "-e", "bash -c \"cd {} && java -jar target/floodlight.jar; "
                                                                 "/bin/bash -i\"".format(
                                                                    self.floodlightSDNControllerPath)])
            else:
                ret = self.__copyConfig('fl_default_config')
                if ret:
                    print("User defined config failed, starting with default config.")
                    # run SDN Controller with default config
                    proc = subprocess.Popen(["gnome-terminal", "-e",
                                             "bash -c \"cd {} && java -jar target/floodlight.jar; /bin/bash -i\"".format(
                                                 self.floodlightSDNControllerPath)])
                else:
                    print("Starting failed.")
        except Exception as e:
            print("Something went wrong " + str(e))

    def __copyConfig(self, SDNControllerSetup):
        """Copy custom configuration before starting SDN controller"""

        try:
            shutil.copy2('/home/user/PycharmProjects/SDNAutomationSystem/sdn_controllers/startup_config/floodlight/{}'.format(SDNControllerSetup),
                         '/home/user/PycharmProjects/SDNControllers/floodlight/src/main/resources/floodlightdefault.properties')
        except Exception as e:
            print("Something went wrong " + str(e))
            return False
        else:
            return True

    def isRunning(self):
        """Returns state of SDN Controller: True/False"""

        try:
            health = self.isHealth()
            return json.loads(health[2])["healthy"]
        except Exception as e:
            print("Something went wrong " + str(e))
            return False

    def isHealth(self):
        """Returns status/health of REST API"""

        health = self.restCall('/wm/core/health/json', {}, 'GET')
        return health

    def showSDNControllerGui(self):
        """Show SDN Controller GUI in web browser"""

        try:
            os.system('gnome-terminal -- bash -c "/bin/su user /usr/bin/firefox http://localhost:8080/ui/index.html"')
        except Exception as e:
            print("Something went wrong " + str(e))

    def addFlow(self, data, path='/wm/staticentrypusher/json'):
        """Insert a static entry
            data: JSON string"""

        try:
            ret = self.restCall(path, data, 'POST')
            return ret[0] == 200
        except Exception as e:
            print("Something went wrong " + str(e))

    def deleteFlow(self, data, path='/wm/staticentrypusher/json'):
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
            switch_ID - static flows on a per-switch basis
            all - all static entries across all switches """

        try:
            ret = self.restCall('/wm/staticentrypusher/list/{}/json'.format(device), {}, 'GET')
            return json.loads(ret[2])
        except Exception as e:
            print("Something went wrong " + str(e))

    def clearFlowTable(self, device):
        """Clear a table of all static entries
        device:
            switch_ID - static flows on a per-switch basis
            all - all static entries across all switches """

        try:
            ret = self.restCall('/wm/staticentrypusher/clear/{}/json'.format(device), {}, 'GET')
            return ret[0] == 200
        except Exception as e:
            print("Something went wrong " + str(e))

    def firewallStatus(self):
        """Get firewall status: enable/disable"""

        try:
            ret = self.restCall('/wm/firewall/module/status/json', {}, 'GET')
            return json.loads(ret[2])
        except Exception as e:
            print("Something went wrong " + str(e))

    def firewallSetStatus(self, status):
        """Set firewall status
        status:
            enable - turn on firewall module
            disable - turn off firewall module"""

        try:
            if status == 'enable':
                print('Enabling firewall...')
                path = '/wm/firewall/module/enable/json'

            elif status == 'disable':
                print('Disabling firewall...')
                path = '/wm/firewall/module/disable/json'

            else:
                return False

            action = 'PUT'
            body = ''

            headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json',
            }
            conn = http.client.HTTPConnection('localhost', 8080)
            conn.request(action, path, body, headers)
            response = conn.getresponse()
            ret = (response.status, response.reason, response.read())
            conn.close()

            return json.loads(ret[2])
        except Exception as e:
            print("Something went wrong " + str(e))

    def firewallAddRule(self, data):
        """Add firewall rule
        data - firewall rule"""

        try:
            ret = self.restCall('/wm/firewall/rules/json', data, 'POST')
            return json.loads(ret[2])
        except Exception as e:
            print("Something went wrong " + str(e))

    def firewallDeleteRule(self, data):
        """Delete firewall rule by rule_ID
        data - rule ID"""

        try:
            ret = self.restCall('/wm/firewall/rules/json', {'ruleid': data}, 'DELETE')
            return json.loads(ret[2])
        except Exception as e:
            print("Something went wrong " + str(e))

    def firewallClearRules(self):
        """Clear all firewall rules on SDN Controller"""

        try:
            rules = self.firewallListRules()
            ret = []
            for rule in rules:
                retRule = self.restCall('/wm/firewall/rules/json', {'ruleid': rule['ruleid']}, 'DELETE')
                ret.append(json.loads(retRule[2]))
            return ret
        except Exception as e:
            print("Something went wrong " + str(e))

    def firewallListRules(self):
        """List firewall rules"""

        try:
            ret = self.restCall('/wm/firewall/rules/json', {}, 'GET')
            return json.loads(ret[2])
        except Exception as e:
            print("Something went wrong " + str(e))

    def addAclRule(self, data):
        """Add ACL rule
        data - ACL rule"""

        try:
            ret = self.restCall('/wm/acl/rules/json', data, 'POST')
            return json.loads(ret[2])
        except Exception as e:
            print("Something went wrong " + str(e))

    def deleteAclRule(self, data):
        """Delete ACL rule by rule_ID
        data - rule ID"""

        try:
            ret = self.restCall('/wm/acl/rules/json', {'ruleid': data}, 'DELETE')
            return ret[0] == 200
        except Exception as e:
            print("Something went wrong " + str(e))

    def clearAclRules(self):
        """Clear all ACL rules on SDN Controller"""

        try:
            ret = self.restCall('/wm/acl/clear/json', {}, 'GET')
            return ret[0] == 204
        except Exception as e:
            print("Something went wrong " + str(e))

    def listAclRules(self):
        """List firewall rules"""

        try:
            ret = self.restCall('/wm/acl/rules/json', {}, 'GET')
            return json.loads(ret[2])
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
    pusher = Floodlight()
    print(pusher.isRunning())

    flow1 = {
        'switch': "00:00:00:00:00:00:00:01",
        "name": "flow_mod_1",
        "cookie": "0",
        "priority": "32768",
        "in_port": "1",
        "active": "true",
        "actions": "output=controller"
    }

    flow2 = {
        'switch': "00:00:00:00:00:00:00:01",
        "name": "flow_mod_2",
        "cookie": "0",
        "priority": "32768",
        "in_port": "2",
        "active": "true",
        "actions": "output=3"
    }

    flow3 = {
        'switch': "00:00:00:00:00:00:00:01",
        "name": "flow_mod_3",
        "cookie": "0",
        "priority": "32768",
        "in_port": "3",
        "active": "true",
        "actions": "output=2"
    }

    flow4 = {
        'switch': "00:00:00:00:00:00:00:01",
        "name": "flow_mod_4",
        "cookie": "0",
        "priority": "32768",
        "in_port": "-1",
        "active": "true",
        "actions": "output=controller"
    }

    objType = {"name": "flow_mod_2"}
    # pusher.clearFlowTable('all')

    # print(pusher.addFlow(flow1))

    # print(pusher.addFlow(flow2))
    # print(pusher.addFlow(flow3))
    # # print(pusher.addFlow(flow4))
    # #
    # print(pusher.listFlowTable('all'))
    # # #
    # pusher.clearFlowTable('all')
    # print(pusher.deleteFlow(objType))
    #
    #
    # print(pusher.listFlowTable('all'))

    # print(pusher.firewallStatus())
    # print(pusher.firewallSetStatus('enable'))
    # print(pusher.firewallStatus())
    #
    # print(pusher.firewallAddRule({"switchid": "00:00:00:00:00:00:00:01"}))
    # print(pusher.firewallAddRule({"src-ip": "10.0.0.1/32", "dst-ip": "10.0.0.3/32"}))
    # print(pusher.firewallAddRule({"src-ip": "10.0.0.3/32", "dst-ip": "10.0.0.1/32"}))

    # print(pusher.firewallClearRules())
    #
    # print(pusher.firewallSetStatus('enable'))
    # print(pusher.firewallStatus())

    # print(pusher.firewallAddRule({"dl-type": "ARP"}))
    # print(pusher.firewallAddRule({"src-ip": "10.123.123.1/32", "dst-ip": "10.0.0.1/32"}))
    # print(pusher.firewallAddRule({"src-ip": "10.0.0.1/32", "dst-ip": "10.123.123.1/32"}))
    #
    # print(pusher.firewallAddRule({"src-ip": "10.123.123.1/32", "dst-ip": "10.0.0.2/32"}))
    # print(pusher.firewallAddRule({"src-ip": "10.0.0.2/32", "dst-ip": "10.123.123.1/32"}))

    # print(pusher.firewallAddRule({"src-ip": "10.0.0.1/32", "dst-ip": "10.123.123.1//32", "nw-proto": "ICMP"}))
    # print(pusher.firewallAddRule({"src-ip": "10.123.123.1//32", "dst-ip": "10.0.0.1/32", "nw-proto": "ICMP"}))

    # print(pusher.firewallAddRule({"src-ip": "10.0.0.1/32", "dst-ip": "10.0.0.3/32", "dl-type": "ARP"}))
    # print(pusher.firewallAddRule({"src-ip": "10.0.0.3/32", "dst-ip": "10.0.0.1/32", "dl-type": "ARP"}))
    #
    # print(pusher.firewallAddRule({"src-ip": "10.0.0.1/32", "dst-ip": "10.0.0.3/32", "nw-proto": "ICMP"}))
    # print(pusher.firewallAddRule({"src-ip": "10.0.0.3/32", "dst-ip": "10.0.0.1/32", "nw-proto": "ICMP"}))
    #
    # print(pusher.firewallAddRule({"src-ip": "10.0.0.2/32", "dst-ip": "10.0.0.3/32", "nw-proto": "ICMP"}))
    # print(pusher.firewallAddRule({"src-ip": "10.0.0.3/32", "dst-ip": "10.0.0.2/32", "nw-proto": "ICMP"}))
    #
    # print(pusher.firewallAddRule({"src-ip": "10.0.0.1/32", "dst-ip": "10.0.0.3/32", "nw-proto": "TCP", "tp-dst": "80", "action": "ALLOW"}))
    # print(pusher.firewallAddRule({"src-ip": "10.0.0.3/32", "dst-ip": "10.0.0.1/32", "nw-proto": "TCP", "tp-src": "80", "action": "ALLOW"}))

    # print(pusher.firewallAddRule({"src-ip": "10.0.0.2/32", "dst-ip": "10.0.0.3/32", "dl-type": "ARP"}))
    # print(pusher.firewallAddRule({"src-ip": "10.0.0.3/32", "dst-ip": "10.0.0.2/32", "dl-type": "ARP"}))

    # print(pusher.firewallAddRule({"src-ip": "10.0.0.2/32", "dst-ip": "10.0.0.3/32", "nw-proto": "TCP", "tp-dst": "80", "action": "DENY"}))
    # print(pusher.firewallAddRule({"src-ip": "10.0.0.3/32", "dst-ip": "10.0.0.2/32", "nw-proto": "TCP", "tp-dst": "80", "action": "DENY"}))

    # print(pusher.firewallAddRule({"src-ip": "10.0.0.2/32", "dst-ip": "10.0.0.3/32", "nw-proto": "TCP", "tp-dst": "80", "action": "ALLOW"}))
    # print(pusher.firewallAddRule({"src-ip": "10.0.0.3/32", "dst-ip": "10.0.0.2/32", "nw-proto": "TCP", "tp-src": "80", "action": "ALLOW"}))




    # print(pusher.firewallListRules())
    # print(pusher.firewallDeleteRule('481861876'))

