import unittest
from src.main.python.ReadFromFile import ReadFromFile
from src.main.python.TestOutput import TestOutput
from src.main.python.TestInput import TestInput

class MainTest(unittest.TestCase):
    def test_play(self):
        readFromFile = ReadFromFile()
        recordedOutput = readFromFile.read("ConsoleOutput.csv")
        testOutput = TestOutput()
        self.assertEqual(recordedOutput, testOutput)


if __name__ == '__main__':
    unittest.main()
