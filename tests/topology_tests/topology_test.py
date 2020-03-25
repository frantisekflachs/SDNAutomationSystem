from abc import abstractmethod
from tests.test import Test


class TopologyTest(Test):

    @abstractmethod
    def execute(self):
        pass
