from sdnControllers.sdnController import SDNController
import config
import subprocess
import os



class Ryu(SDNController):

    def run(self, OFVersion, SDNControllerSetup):

        runOptions = ''
        for o in SDNControllerSetup:
            runOptions += ' ' + o

        os.system('gnome-terminal -- bash -c "cd {}/ryu && /bin/ryu-manager{} && bash"'.format(config.SDNControllersPath, runOptions))

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
