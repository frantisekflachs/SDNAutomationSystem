from abc import abstractmethod

from networkTopology.networkTopology import NetworkTopology


class VirtualTopology(NetworkTopology):

    @abstractmethod
    def run(self):
        pass
