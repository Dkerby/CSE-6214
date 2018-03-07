import random

class NumberList():
    def __init__(self, numbers = []):
        self.numbers = numbers

    def generateRandom(self, size):
        self.numbers = random.sample(xrange(1, 10000), size)