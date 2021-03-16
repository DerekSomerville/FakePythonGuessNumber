from src.main.python.Output import Output

class TestOutput(Output):

    outputlist = []

    def setOutputList(self,outputList):
        self.outputlist = outputList

    def output(self, request):
        self.outputlist.append(request)

    def getOutputList(self):
        return self.outputlist