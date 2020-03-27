import subprocess

from sdnControllers.sdnController import SDNController
import config
import os
import http.client
import json


class Floodlight(SDNController):

    def run(self, OFVersion, SDNControllerSetup):
        """Run SDN controller in new terminal window"""
        # os.system('gnome-terminal -- bash -c "cd {}/floodlight && java -jar target/floodlight.jar && bash"'.format(
        #     config.SDNControllersPath))
        proc = subprocess.Popen(["gnome-terminal", "-e", "bash -c \"cd {}/floodlight && java -jar target/floodlight.jar; /bin/bash -i\"".format(
            config.SDNControllersPath)])
        pid = proc.pid
        print(pid)

        # subprocess.run(["gnome-terminal", "-e", "bash -c \"/bin/ls; /bin/bash -i\""])

    def showSDNControllerGui(self):
        os.system('gnome-terminal -- bash -c "/bin/su user /usr/bin/firefox http://localhost:8080/ui/index.html"')

    def addFlow(self, data):
        """Insert a static entry
        data: JSON string"""
        ret = self.restCall('/wm/staticentrypusher/json', data, 'POST')
        return ret[0] == 200

    def deleteFlow(self, data):
        """Delete a static entry
        data: JSON string"""
        ret = self.restCall('/wm/staticentrypusher/json', data, 'DELETE')
        return ret[0] == 200

    def listFlowTable(self, device):
        """Get a list of all static entries
        device:
            switch_ID - static flows on a per-switch basis
            all - all static entries across all switches """

        ret = self.restCall('/wm/staticentrypusher/list/{}/json'.format(device), {}, 'GET')
        return json.loads(ret[2])

    def clearFlowTable(self, device):
        """Clear a table of all static entries
        device:
            switch_ID - static flows on a per-switch basis
            all - all static entries across all switches """

        ret = self.restCall('/wm/staticentrypusher/clear/{}/json'.format(device), {}, 'GET')
        return ret[0] == 200

    def firewallStatus(self):
        """Get firewall status: enable/disable"""
        ret = self.restCall('/wm/firewall/module/status/json', {}, 'GET')
        return json.loads(ret[2])

    def firewallSetStatus(self, status):
        """Set firewall status
        status:
            enable - turn on firewall module
            disable - turn off firewall module"""

        if status == 'enable':
            print('Enabling firewal...')
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
        conn = http.client.HTTPConnection(config.SDNControllerIP, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        conn.close()

        return json.loads(ret[2])

    def firewallAddRule(self, data):
        """Add firewall rule
        data - firewall rule"""
        ret = self.restCall('/wm/firewall/rules/json', data, 'POST')
        return json.loads(ret[2])

    def firewallDeleteRule(self, data):
        """Delete firewall rule by rule_ID
        data - rule ID"""
        ret = self.restCall('/wm/firewall/rules/json', {'ruleid': data}, 'DELETE')
        return json.loads(ret[2])

    def firewallListRules(self):
        """List firewall rules"""
        ret = self.restCall('/wm/firewall/rules/json', {}, 'GET')
        return json.loads(ret[2])

    def restCall(self, path, data, action):
        """Rest Call for SDN controller
        data: JSON string
        action: GET|POST|DELETE"""

        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
        }
        body = json.dumps(data)
        conn = http.client.HTTPConnection(config.SDNControllerIP, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        conn.close()
        return ret


if __name__ == "__main__":
    pusher = Floodlight()

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

    objType = {"name": "flow_mod_2"}

    print(pusher.addFlow(flow1))
    print(pusher.addFlow(flow2))
    #
    print(pusher.listFlowTable('all'))
    #
    pusher.clearFlowTable('all')
    print(pusher.deleteFlow(objType))
    #
    #
    print(pusher.listFlowTable('all'))

    print(pusher.firewallStatus())
    print(pusher.firewallSetStatus('enable'))
    print(pusher.firewallStatus())

    print(pusher.firewallAddRule({"src-ip": "10.0.0.3/32", "dst-ip": "10.0.0.7/32"}))
    print(pusher.firewallListRules())
    print(pusher.firewallDeleteRule('481861876'))
