from sdnControllers.sdnController import SDNController
import config
import os


class Pox(SDNController):

    def run(self, OFVersion):
        if OFVersion == '10':
            os.system('gnome-terminal -- bash -c "{}/pox/pox.py --verbose py samples.pretty_log forwarding.l2_learning '
                  'openflow.of_01 --port=6653 && bash"'.format(config.SDNControllersPath))

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
