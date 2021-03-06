from abc import ABC, abstractmethod


class SDNController(ABC):
    
    @abstractmethod
    def run(self, SDNControllerSetup):
        pass

    @abstractmethod
    def isRunning(self):
        pass

    @abstractmethod
    def showSDNControllerGui(self):
        pass

    @abstractmethod
    def addFlow(self, data, path):
        pass

    @abstractmethod
    def deleteFlow(self, data, path):
        pass

    @abstractmethod
    def listFlowTable(self, device):
        pass

    @abstractmethod
    def clearFlowTable(self, device):
        pass