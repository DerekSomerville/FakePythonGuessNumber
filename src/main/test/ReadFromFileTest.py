import unittest
from src.main.python.ReadFromFile import ReadFromFile


class ReadFromFileTest(unittest.TestCase):
    readFromFile = ReadFromFile()
    def test_read(self):
        self.assertEqual(['3','4','8'], self.readFromFile.read("ConsoleInput.csv"))


if __name__ == '__main__':
    unittest.main()
