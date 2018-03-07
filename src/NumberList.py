import random

class NumberList():
    def __init__(self, numbers = []):
        self.numbers = numbers
        self.length = len(numbers)

    def generateRandom(self, size):
        self.numbers = random.sample(xrange(1, 10000), size)
        self.length = len(self.numbers)

    def importListFromFile(self, filename):
        f = open(filename, "r")
        tempList = []

        line = f.readline()
        line = line.replace(" ", "")
        tempList = line.split(',')
        self.numbers = tempList

        f.close()

    def exportListToFile(self, filename):
        file = open(filename,"w")

        for num in self.numbers:
            file.write(str(num) + ',')

        file.close()