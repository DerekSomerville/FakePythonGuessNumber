from src.main.python.Input import Input
from src.main.python.WriteToFile import WriteToFile

class ConsoleInput(Input):

    writeToFile = True
    userInputWriteToFile = WriteToFile("ConsoleInput.csv")

    def getInputString(self, request):
        userInput = input(request)
        if self.writeToFile:
            self.userInputWriteToFile.writeToFile(userInput)
        return userInput
