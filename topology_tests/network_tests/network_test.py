from abc import abstractmethod


class NetworkTest:

    @abstractmethod
    def execute(self, params):
        pass
