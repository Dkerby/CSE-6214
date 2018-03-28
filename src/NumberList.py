import random

class NumberList(object):
    def __init__(self, numbers = []):
        self.numbers = numbers
        self.length = len(numbers)

    def generateRandom(self, size):
        self.numbers = random.sample(range(1, size+1), size)
        self.length = len(self.numbers)

    def importListFromFile(self, filename):
        f = open(filename, "r")
        tempList = []

        line = f.readline()
        line = line.replace(" ", "")
        tempList = line.split(',')
        self.numbers = tempList

        f.close()
		
    def importListFromText(self, fileText):
        fileText = fileText.decode("utf-8") 
        fileText = fileText.replace(" ", "")
        self.numbers = fileText.split(',')
		
        for i in range(len(self.numbers)):
            self.numbers[i] = int(self.numbers[i])
			
        self.length = len(self.numbers)

    def exportListToFile(self, filename):
        file = open(filename,"w")

        for num in self.numbers:
            file.write(str(num) + ',')

        file.close()
