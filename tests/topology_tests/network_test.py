from abc import abstractmethod
from tests.topology_test import TopologyTest


class NetworkTest(TopologyTest):

    @abstractmethod
    def execute(self):
        pass
