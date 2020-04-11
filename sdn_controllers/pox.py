import requests

from sdn_controllers.sdnController import SDNController

import config
import os
import http.client
import json
from urllib.parse import urlencode
import pycurl
import subprocess


class Pox(SDNController):

    def run(self, SDNControllerSetup):

        if not SDNControllerSetup:
            os.system(
                'gnome-terminal -- bash -c "{}/pox/pox.py --verbose py samples.pretty_log forwarding.l2_learning '
                'openflow.of_01 --port=6653 && bash"'.format(config.SDNControllersPath))
        else:
            runOptions = ''
            for o in SDNControllerSetup:
                runOptions += ' ' + o
            print('gnome-terminal -- bash -c "{}/pox/pox.py {} && bash"'.format(config.SDNControllersPath,
                                                                                runOptions))
            os.system('gnome-terminal -- bash -c "{}/pox/pox.py {} && bash"'.format(config.SDNControllersPath,
                                                                                    runOptions))

    def showSDNControllerGui(self):
        """Show SDN Controller GUI in web browser"""

        os.system('gnome-terminal -- bash -c "/bin/su user /usr/bin/firefox http://127.0.0.1:8000/"')

    def addFlow(self, data):
        """Insert a static entry
        data: JSON string"""

        ret = self.restCall('/OF/', {"method": "set_table", "params": data, "id": 0})
        return ret

    def deleteFlow(self, data):
        print("Not implemented.")
        pass

    def listFlowTable(self, device):
        """Get a list of all static entries
        device:
            switch_ID - static flows on a per-switch basis"""

        ret = self.restCall('/OF/pretty/', {"method": "get_flow_stats", "params": {"dpid": device}, "id": 0})
        return ret

    def clearFlowTable(self, device):
        print("Not implemented.")
        pass

    def firewallStatus(self):
        print("Not implemented.")
        pass

    def firewallSetStatus(self, status):
        print("Not implemented.")
        pass

    def firewallAddRule(self, data):
        print("Not implemented.")
        pass

    def firewallDeleteRule(self, data):
        print("Not implemented.")
        pass

    def firewallListRules(self):
        print("Not implemented.")
        pass

    def restCall(self, path, data):
        """Rest Call for SDN controller
        path: path for rest call
        data: JSON string"""

        header = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
        }

        ret = requests.post('http://127.0.0.1:8000' + path, data=json.dumps(data), headers=header)
        return ret.text


if __name__ == "__main__":
    pusher = Pox()

    # curl -i -X POST -d '{"method":"get_flow_stats","params":{"dpid":"00-00-00-00-00-01"},"id":0}'  http://127.0.0.1:8000/OF/pretty
    # curl -i -X POST -d '{"method":"get_switches","id":0}'  http://127.0.0.1:8000/OF/pretty
    # curl -i -X POST -d '{"method":"get_switch_desc","params":{"dpid":"00-00-00-00-00-01"},"id":0}'  http://127.0.0.1:8000/OF/pretty

    # curl -i -X POST -d '{"method":"set_table","params":{"dpid":"00-00-00-00-00-01","flows":[{"actions": [{"type":"OFPAT_OUTPUT","port":2}],"match": {"dl_type": "IP","in_port":1 }}]}}' http://127.0.0.1:8000/OF/
    # curl -i -X POST -d '{"method":"set_table","params":{"dpid":"00-00-00-00-00-01","flows":[{"actions": [{"type":"OFPAT_OUTPUT","port":2}],"match": {"dl_type": "IP","in_port":1 }},{"actions":[{"type":"OFPAT_OUTPUT","port":"OFPP_ALL"}]}]}}' http://127.0.0.1:8000/OF/
    # curl -i -X POST -d '{"method":"set_table","params":{"dpid":"00-00-00-00-00-01","flows":[{"actions": [{"type":"OFPAT_OUTPUT","port":2}],"match": {"dl_type": "IP","nw_dst":"192.168.42.0/255.255.255.0" }}]}}' http://127.0.0.1:8000/OF/
    # curl -i -X POST -d '{"method":"set_table","params":{"dpid":"00-00-00-00-00-01","flows":[{"actions":[{"type":"OFPAT_OUTPUT","port":"OFPP_ALL"}],"match":{}}]},"id":0}' http://127.0.0.1:8000/OF/

    print(pusher.listFlowTable('00-00-00-00-00-01'))
    print(pusher.addFlow({"dpid": "00-00-00-00-00-01", "flows": [{"actions": [{"type": "OFPAT_OUTPUT", "port": 1}], "match": {"dl_type": "IP", "in_port": 1}}]}))
    print(pusher.listFlowTable('00-00-00-00-00-01'))
