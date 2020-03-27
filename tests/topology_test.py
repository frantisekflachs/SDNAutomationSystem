from abc import ABC, abstractmethod


class TopologyTest(ABC):

    @abstractmethod
    def execute(self):
        pass
