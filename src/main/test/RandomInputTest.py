import unittest
from src.main.python.RandomInput import RandomInput

class RandomInputTest(unittest.TestCase):


    def testGet(self):
        randomInput = RandomInput()
        self.assertTrue(randomInput.getInputInt("") <= randomInput.getMaxNumber())