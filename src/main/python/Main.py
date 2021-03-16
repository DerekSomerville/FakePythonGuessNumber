from ConsoleInput import ConsoleInput
from ConsoleOutput import ConsoleOutput
from RandomInput import RandomInput

class Main:
    output = ConsoleOutput();
    input = ConsoleInput();
    random = RandomInput();

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
