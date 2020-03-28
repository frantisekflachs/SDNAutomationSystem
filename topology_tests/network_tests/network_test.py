from abc import abstractmethod
from topology_tests.topology_test import TopologyTest


class NetworkTest(TopologyTest):

    @abstractmethod
    def execute(self):
        pass
