from src.main.python.Output import Output
from src.main.python.WriteToFile import WriteToFile

class ConsoleOutput(Output):

    writeToFile = True
    outputWriteToFile = WriteToFile("ConsoleOutput.csv")

    def output(self, output):
        if self.writeToFile:
            self.outputWriteToFile.writeToFile(output)
        print(output)
