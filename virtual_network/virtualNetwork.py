from abc import ABC, abstractmethod

class VirtualNetwork(ABC):

    @abstractmethod
    def run(self):
        pass
