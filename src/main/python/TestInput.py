from src.main.python.Input import Input

class TestInput(Input):

    inputList = []

    def getInputString(self, request):
        return self.inputList.pop(0)
