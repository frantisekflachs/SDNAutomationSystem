from abc import abstractmethod
from topology_tests.topology_test import TopologyTest


class SDNControllerTest(TopologyTest):

    @abstractmethod
    def execute(self):
        pass