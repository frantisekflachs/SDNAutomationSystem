from sdn_controllers.sdnController import SDNController
# import config
import os


class Opendaylight(SDNController):

    def run(self, SDNControllerSetup):
        # os.system('gnome-terminal -- bash -c "{}/opendaylight/bin/karaf&& bash"'.format(config.SDNControllersPath))
        pass

    def showSDNControllerGui(self):
        pass

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
