from sdn_controllers.sdnController import SDNController

import requests
import config
import os
import json


class Pox(SDNController):
    """POX SDN Controller"""

    def run(self, SDNControllerSetup):
        """Run SDN controller in new terminal window"""

        try:
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
        except Exception as e:
            print("Something went wrong " + str(e))

    def showSDNControllerGui(self):
        """Show SDN Controller GUI in web browser"""

        try:
            os.system('gnome-terminal -- bash -c "/bin/su user /usr/bin/firefox http://127.0.0.1:8000/"')
        except Exception as e:
            print("Something went wrong " + str(e))

    def addFlow(self, data):
        """Insert a static entry
            data: JSON string"""

        try:
            ret = self.restCall('/OF/', {"method": "set_table", "params": data, "id": 0})
            return ret
        except Exception as e:
            print("Something went wrong " + str(e))

    def deleteFlow(self, data):
        """Delete a static entry
            data: JSON string"""

        print("Not implemented.")

    def listFlowTable(self, device):
        """Get a list of all static entries
        device:
            switch_ID - static flows on a per-switch basis"""

        try:
            ret = self.restCall('/OF/pretty/', {"method": "get_flow_stats", "params": {"dpid": device}, "id": 0})
            return ret
        except Exception as e:
            print("Something went wrong " + str(e))

    def clearFlowTable(self, device):
        """Clear a table of all static entries
        device:
            switch_ID - static flows on a per-switch basis"""

        print("Not implemented.")

    def restCall(self, path, data, action):
        """Rest Call for SDN controller
            path: REST CALL URL
            data: JSON string
            action: GET|POST|DELETE"""

        try:
            header = {
                'Content-type': 'application/json',
                'Accept': 'application/json',
            }

            ret = requests.post('http://127.0.0.1:8000' + path, data=json.dumps(data), headers=header)
            return ret.text
        except Exception as e:
            print("Something went wrong " + str(e))


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
