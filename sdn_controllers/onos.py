import time

from sdn_controllers.sdnController import SDNController
import config
import os


class Onos(SDNController):

    def run(self, SDNControllerSetup):
        os.system('gnome-terminal -- bash -c "export TERM=xterm-color && {}/onos/bin/onos-service start && bash"'.format(config.SDNControllersPath))
        # time.sleep(20)

    def showSDNControllerGui(self):
        """Show SDN Controller GUI in web browser"""
        os.system('gnome-terminal -- bash -c "/bin/su user /usr/bin/firefox http://127.0.0.1:8181/onos/ui/login.html"')

    def addFlow(self, data):
        pass

    def deleteFlow(self, data):
        pass

    def listFlowTable(self, device):
        pass

    def clearFlowTable(self, device):
        pass

    def firewallStatus(self):
        pass

    def firewallSetStatus(self, status):
        pass

    def firewallAddRule(self, data):
        pass

    def firewallDeleteRule(self, data):
        pass

    def firewallListRules(self):
        pass
