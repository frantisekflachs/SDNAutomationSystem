from abc import ABC, abstractmethod


class NetworkTopology(ABC):

    @abstractmethod
    def run(self):
        pass
e