from sdnControllers.sdnController import SDNController
import config
import os


class Onos(SDNController):

    def run(self, OFVersion, SDNControllerSetup):
        os.system('gnome-terminal -- bash -c "{}/onos/bin/onos-service start && bash"'.format(config.SDNControllersPath))

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
