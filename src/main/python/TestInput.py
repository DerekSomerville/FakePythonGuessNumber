from src.main.python.Input import Input

class TestInput(Input):

    inputList = []

    def getInputString(self, request):
        return self.inputList.pop(0)

    def setInputList(self,inputList):
        self.inputList = inputList