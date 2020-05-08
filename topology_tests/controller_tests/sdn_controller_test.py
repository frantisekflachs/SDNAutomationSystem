from abc import abstractmethod


class SDNControllerTest:

    @abstractmethod
    def execute(self, params, SDNController):
        pass
