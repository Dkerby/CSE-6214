import NumberList as nl
import time, sys

class Algorithm(object):
	data=None
	state=None
	selectedAlgo=''
	i=0
	j=0

	def __init__(self):
		self.data=nl.NumberList()
		self.data.generateRandom(100)
		self.selectedAlgo="insertion"
		self.i=1
		self.j=1

	def iterateInsertionSort(self):
		if(j>0 and self.data.numbers[j-1]>self.data.numbers[i]
			self.data.numbers[j]=self.data.numbers[j-1]
			self.j-=1
		self.data.numbers[j]=self.data.numbers[i]
		self.i+=1
			
	def step(self):
		if(selectedAlgo=="insertion"):
			if(self.i<self.data.length):
				self.j=self.i
				self.iterateInsertionSort()
			
	def play(self):
		while(i<self.data.length):
			time.sleep(.25)
			self.step()
		
		
if __name__ == '__main__':
	x=Algorithm()
	usr_input=0
	while(True):
		sys.stdout.flush()
		print(x.data)
		if(usr_input):
			x.step()
		else:
			usr_input=input("hit enter to step. type anything to play")
