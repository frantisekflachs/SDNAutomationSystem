from abc import ABC, abstractmethod


class SDNController(ABC):

    @abstractmethod
    def run(self, OFVersion, SDNControllerSetup):
        pass

    @abstractmethod
    def showSDNControllerGui(self):
        pass

    @abstractmethod
    def addFlow(self, data):
        pass

    @abstractmethod
    def deleteFlow(self, data):
        pass

    @abstractmethod
    def listFlowTable(self, device):
        pass

    @abstractmethod
    def clearFlowTable(self, device):
        pass

    @abstractmethod
    def firewallStatus(self):
        pass

    @abstractmethod
    def firewallSetStatus(self, status):
        pass

    @abstractmethod
    def firewallAddRule(self, data):
        pass

    @abstractmethod
    def firewallDeleteRule(self, data):
        pass

    @abstractmethod
    def firewallListRules(self):
        pass