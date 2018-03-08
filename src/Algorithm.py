from __future__ import print_function
import time, sys,os
import NumberList as nl
import random

class InsertionStatus(object):
	def __init__(self, data):
		self.i=1
		self.j=1
		self.cval=data.numbers[self.i]
		self.length=len(data.numbers)

class Algorithm(object):

	def __init__(self):
		self.data=nl.NumberList()
		self.data.generateRandom(150)
		self.algo=InsertionStatus(self.data)
		self.complete=False

	def iterateInsertionSort(self):
		if(self.algo.j>0 and self.data.numbers[self.algo.j-1]>self.algo.cval):
			self.data.numbers[self.algo.j]=self.data.numbers[self.algo.j-1]
			self.algo.j-=1
		else:
			self.data.numbers[self.algo.j]=self.algo.cval
			self.algo.i+=1
			if(self.algo.i<self.algo.length):
				self.algo.cval=self.data.numbers[self.algo.i]
				self.algo.j=self.algo.i
			else:
				
				self.algo.i-=1
				self.complete=True
			
	def step(self):
		if(isinstance(self.algo, InsertionStatus)):
			if(not self.complete):
				self.iterateInsertionSort()
			
	def play(self):
		#maybe move this into main
		return
		
		
if __name__ == '__main__':
	x=Algorithm()
	while(not x.complete):
		x.step()
		i = x.algo.i #if x.algo.i<x.algo.length-1 else x.algo.i-1
		j = x.algo.j #if x.algo.j<x.algo.length-1 else x.algo.i-1
		output="Data:\n" + str(x.data.numbers[:j]) + '\x1b[0;37;41m' + str(x.data.numbers[j]) + '\x1b[0m' + str(x.data.numbers[x.algo.j+1:x.algo.i]) + '\x1b[0;30;44m' + str(x.data.numbers[i]) + '\x1b[0m' + str(x.data.numbers[i+1:]) +"\nj: " + str(x.algo.j) +"\ni: " + str(x.algo.i)
		
		os.system('clear')
		print(output)
		#print(x.algo.i)
		#print(x.algo.j)
		#raw_input("<hit enter to step>")
		#x.step()
		time.sleep(.05)
	print(x.data.numbers)
