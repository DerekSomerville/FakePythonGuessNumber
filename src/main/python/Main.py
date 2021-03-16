from src.main.python.ConsoleInput import ConsoleInput
from src.main.python.ConsoleOutput import ConsoleOutput
from src.main.python.RandomInput import RandomInput

class Main:
    output = None
    input = None
    random = None

    def __init__(self,output=None,input=None,random=None):
        if output == None:
            self.output = ConsoleOutput()
        else:
            self.output = output
        if input == None:
            self.input = ConsoleInput()
        else:
            self.input = input
        if random == None:
            self.random = RandomInput()
        else:
            self.random = random

    def play(self):
        result = 0;

        self.output.output("Please guess a random number, enter a larger number to stop")
        while result <= self.random.getMaxNumber():
            computerNumber = self.random.getInputInt("")
            result = self.input.getInputInt("Please guess a number from 0 to " + str(self.random.getMaxNumber()))
            if result == computerNumber:
                self.output.output("Correct")
            elif result < self.random.getMaxNumber():
                self.output.output("Wrong")

    def setOutput(self,output):
        self.output = output

    def setInput(self,input):
        self.input = input

    def setRandom(self,random):
        self.random = random

    def main():
       main = Main()
       main.play()


if __name__ == "__main__":
    Main.main()
