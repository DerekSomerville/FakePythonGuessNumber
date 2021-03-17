import unittest
from src.main.python.ReadFromFile import ReadFromFile
from src.main.python.TestOutput import TestOutput
from src.main.python.TestInput import TestInput
from src.main.python.Main import Main

class MainTestBeforeAfter(unittest.TestCase):

    def getMain(self, testOutput):
        readFromFile = ReadFromFile()
        userTestInput = TestInput()
        userTestData = readFromFile.read("ConsoleInput.csv")
        userTestInput.setInputList(userTestData)
        randomTestInput = TestInput()
        randomTestData = readFromFile.read("RandomInput.csv")
        randomTestInput.setInputList(randomTestData)
        main = Main(testOutput,userTestInput,randomTestInput)
        return main

    def test_play(self):
        readFromFile = ReadFromFile()
        recordedOutput = readFromFile.read("ConsoleOutput.csv")
        testOutput = TestOutput()
        main = self.getMain(testOutput)
        main.play();
        print("Recorded Output: ",recordedOutput)
        print("TestOutput: ",testOutput.getOutputList())
        self.assertEqual(recordedOutput, testOutput.getOutputList())


if __name__ == '__main__':
    unittest.main()
