import unittest
from src.main.python.ReadFromFile import ReadFromFile
from src.main.python.TestOutput import TestOutput
from src.main.python.TestInput import TestInput
from src.main.python.Main import Main

class MainTest(unittest.TestCase):
    def test_play(self):
        readFromFile = ReadFromFile()
        recordedOutput = readFromFile.read("ConsoleOutput.csv")
        testOutput = TestOutput()
        main = Main()
        main.play();
        print("Recorded Output: ",recordedOutput)
        print("TestOutput: ",testOutput.getOutputList())
        self.assertEqual(recordedOutput, testOutput.getOutputList())


if __name__ == '__main__':
    unittest.main()
