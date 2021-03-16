from src.main.python.Output import Output

class TestOutput(Output):

    outputlist = []

    def setOutputList(self,outputList):
        self.outputlist = outputList

    def print(self, request):
        self.outputlist.append(request)
