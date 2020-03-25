from sdnControllers.sdnController import SDNController
import config
import subprocess
import os



class Ryu(SDNController):

    def run(self, OFVersion):
        print(OFVersion)
        os.system('gnome-terminal -- bash -c "/bin/ryu-manager --verbose --observe-links {}/ryu/ryu/app/gui_topology/gui_topology.py '
                  '{}/ryu/ryu/app/simple_switch_{}.py && bash"'.format(config.SDNControllersPath,
                                                                       config.SDNControllersPath,
                                                                       OFVersion))

    def showSDNControllerGui(self):
        os.system('gnome-terminal -- bash -c "/bin/su user /usr/bin/firefox http://localhost:8080/"')

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
