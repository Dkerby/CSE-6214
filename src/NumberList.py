import random

class NumberList(object):
	def __init__(self, numbers = []):
		self.numbers = numbers
		self.length=0

	def generateRandom(self, size):
		self.numbers = random.sample(xrange(1, 10000), size)
		self.length=len(self.numbers)
