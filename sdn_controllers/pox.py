from sdn_controllers.sdnController import SDNController

import config
import os


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
            os.system(
                'gnome-terminal -- bash -c "{}/pox/pox.py {} && bash"'.format(config.SDNControllersPath,
                                                                              runOptions))

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
