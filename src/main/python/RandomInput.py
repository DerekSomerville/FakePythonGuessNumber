from src.main.python.Input import Input
from random import randint
from src.main.python.WriteToFile import WriteToFile

class RandomInput(Input):

    writeToFile = True
    inputWriteToFile = WriteToFile("RandomInput.csv")
    maxNumber = 5

    def getInputString(self, request):
        return self.getInputInt()

    def getMaxNumber(self):
        return self.maxNumber

    def getInputInt(self, request):
        rand = randint(0, self.maxNumber)
        if self.writeToFile:
            self.inputWriteToFile.writeToFile(rand)
        return rand
