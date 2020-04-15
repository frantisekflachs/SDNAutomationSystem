from sdn_controllers.sdnController import SDNController
import config

import os


class Onos(SDNController):
    """ONOS SDN Controller"""

    def run(self, SDNControllerSetup):
        """Run SDN controller in new terminal window"""

        try:
            os.system('gnome-terminal -- bash -c "export TERM=xterm-color && {}/onos/bin/onos-service start && bash"'.format(config.SDNControllersPath))
        except Exception as e:
            print("Something went wrong " + str(e))

    def showSDNControllerGui(self):
        """Show SDN Controller GUI in web browser"""

        try:
            os.system('gnome-terminal -- bash -c "/bin/su user /usr/bin/firefox http://127.0.0.1:8181/onos/ui/login.html"')
        except Exception as e:
            print("Something went wrong " + str(e))

    def addFlow(self, data):
        """Insert a static entry
            data: JSON string"""

        try:
            pass
        except Exception as e:
            print("Something went wrong " + str(e))

    def deleteFlow(self, data):
        """Delete a static entry
            data: JSON string"""

        try:
            pass
        except Exception as e:
            print("Something went wrong " + str(e))

    def listFlowTable(self, device):
        """Get a list of all static entries
        device:
            switch_ID - static flows on a per-switch basis"""

        try:
            pass
        except Exception as e:
            print("Something went wrong " + str(e))

    def clearFlowTable(self, device):
        """Clear a table of all static entries
        device:
            switch_ID - static flows on a per-switch basis"""

        try:
            pass
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
    pusher = Onos()

