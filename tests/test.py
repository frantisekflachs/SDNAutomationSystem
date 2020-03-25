from abc import ABC, abstractmethod


class Test(ABC):

    @abstractmethod
    def execute(self):
        pass
