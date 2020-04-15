from sdn_controllers.sdnController import SDNController

import os


class Opendaylight(SDNController):
    """OpenDaylight SDN Controller"""

    def run(self, SDNControllerSetup):
        """Run SDN controller in new terminal window"""
        # os.system('gnome-terminal -- bash -c "{}/opendaylight/bin/karaf&& bash"'.format(config.SDNControllersPath))
        pass

    def showSDNControllerGui(self):
        """Show SDN Controller GUI in web browser"""

        pass

    def addFlow(self, data):
        """Insert a static entry
            data: JSON string"""

        pass

    def deleteFlow(self, data):
        """Delete a static entry
            data: JSON string"""

        pass

    def listFlowTable(self, device):
        """Get a list of all static entries
        device:
            switch_ID - static flows on a per-switch basis"""

        pass

    def clearFlowTable(self, device):
        """Clear a table of all static entries
        device:
            switch_ID - static flows on a per-switch basis"""

        pass

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
    pusher = Opendaylight()
