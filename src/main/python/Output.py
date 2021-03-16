from abc import ABC, abstractmethod

class Output(ABC):

    outputlist = []

    @abstractmethod
    def output(self, request):
        pass
