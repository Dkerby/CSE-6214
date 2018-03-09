from __future__ import print_function

import time,os #time used for waiting, os used for clearing the cmdline output
import NumberList as nl #holds the data

#This class holds all the information so that the algorithm
#knows where it's place in the sort is between iterations/steps
class InsertionStatus(object):
	def __init__(self, data):
		self.i=1
		self.j=1
		self.cval=data.numbers[self.i]


#Main Algorithm class which implements the stepping and sorting
#Also holds State and NumberList objects
class Algorithm(object):

	def __init__(self):
		self.data=nl.NumberList()#Create the NumberList obj
		self.data.generateRandom(150) #populates NumberList with random data. Used for testing...
		self.algo=InsertionStatus(self.data) #Holds InsertionSort's information
		self.complete=False #complete flag so that step() knows when to stop

        #implementation of insertion sort where information is held between iterations
	def iterateInsertionSort(self):

                # if ( j > 0 && array[j-1] > cval ):
		if(self.algo.j>0 and self.data.numbers[self.algo.j-1]>self.algo.cval):

                        # array[j]=array[j-1]
			self.data.numbers[self.algo.j]=self.data.numbers[self.algo.j-1]

			# j--
			self.algo.j-=1
		else:

                        # array[j] = cval
			self.data.numbers[self.algo.j]=self.algo.cval

			# i++
			self.algo.i+=1

			# if ( i < len(array) )
			if(self.algo.i<self.data.length):

                                # cval = array[i]
				self.algo.cval=self.data.numbers[self.algo.i]

				# j = i
				self.algo.j=self.algo.i
			else:

				# i--
				self.algo.i-=1 #array[i] will thow an error on output because i is out of index range when finished

				# sort is complete
				self.complete=True

	#does one iteration of the selected algorithm	
	def step(self):

                #if self.algo is an instance of InsertionStatus, then do this one
		if(isinstance(self.algo, InsertionStatus)):

                        #if the complete flag is not set, then keep doing the algorithm
			if(not self.complete):
				self.iterateInsertionSort()
				
                #TODO: elifs for the other algorithms go here
			
	def play(self):
		#maybe move this into main
		return
		

#Used for testing. You can probably move some of this into main.py for the finished program
if __name__ == '__main__':

        #creates algorithm obj
	x=Algorithm()

	#while algorithm is not complete, keep on steppin'
	while(not x.complete):

		x.step()

		#local variables for i and j
		i = x.algo.i
		j = x.algo.j

		#format the output string. the "x1b--m values are for colors
		output="Data:\n" + str(x.data.numbers[:j]) + '\x1b[0;37;41m' + str(x.data.numbers[j]) + '\x1b[0m' + str(x.data.numbers[x.algo.j+1:x.algo.i]) + '\x1b[0;30;44m' + str(x.data.numbers[i]) + '\x1b[0m' + str(x.data.numbers[i+1:]) +"\nj: " + str(x.algo.j) +"\ni: " + str(x.algo.i)

		#clear stdout
		os.system('clear')

		#print to cmdline
		print(output)

		#uncomment the following to wait for input for each step:
		#raw_input("<hit enter to step>")

		#wait for a bit so that the output can actually be seen
		time.sleep(.05)

	#One last print to check and make sure the above output is correct.
	print(x.data.numbers)
