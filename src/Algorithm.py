from __future__ import print_function

import time,os #time used for waiting, os used for clearing the cmdline output
import NumberList as nl #holds the data

##############################################################################
#These classes hold all the information so that the algorithm                #
#knows where it's place in the sort is between iterations/steps              #
##############################################################################

#Stack class so that we can keep track of subarrays
class Stack:
	def __init__(self, items=[]):
		self.items = items

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def top(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

#Insertion Sort Data
class InsertionStatus(object):
	def __init__(self, data):
		self.i=1
		self.j=1
		self.cval=data.numbers[self.i]

#Quick Sort Data
class QuickSortStatus(object):
	def __init__(self, data):
		self.i=-1
		self.j=0

		#these are stacks so that the algorithm can hold a trace/history
		#of the subarrays.
		self.begin=Stack([0])
		self.end=Stack([(len(data.numbers)-1)])

		#pivot defaults to last element of subarray
		self.p=(len(data.numbers)-1)



################################################################################
# THE MAIN ALGORITHM CLASS -- implements the stepping and sorting for each     #
# algorithm and also holds State and NumberList objects                        #
################################################################################

class Algorithm(object):

	#*****************************************************************************************
	#CONSTRUCTOR

	def __init__(self):
		self.data=nl.NumberList()#Create the NumberList obj
		self.data.generateRandom(150) #populates NumberList with random data. Used for testing...
		self.algo=QuickSortStatus(self.data) #Holds InsertionSort's information
		self.complete=False #complete flag so that step() knows when to stop


        #*****************************************************************************************
	#INSERTION SORT

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


	#*****************************************************************************************
	#QUICK SORT

	def iterateQuickSort(self):
		
		#if the subarray is not sorted
		if(self.algo.begin.top()<self.algo.end.top()):

			#if j is not at the end of the subarray
			if(self.algo.j<self.algo.end.top()):

				#if array[j] <= array[pivot]
				if(self.data.numbers[self.algo.j]<=self.data.numbers[self.algo.p]):
					
					#i++
					self.algo.i+=1

					#swap array[i] and array[j]
					temp=self.data.numbers[self.algo.j]
					self.data.numbers[self.algo.j]=self.data.numbers[self.algo.i]
					self.data.numbers[self.algo.i]=temp

				#j++
				self.algo.j+=1

			#if j has iterated through the subarray
			else:
				
				#swap array[i+1] and array[pivot]
				temp=self.data.numbers[(self.algo.i+1)]
				self.data.numbers[(self.algo.i+1)]=self.data.numbers[self.algo.end.top()]
				self.data.numbers[self.algo.end.top()]=temp

				#pop top of begin stack
				temp_begin=self.algo.begin.pop()

				#push the beginning of the right subarray to the begin stack
				self.algo.begin.push(self.algo.i+2)

				#push the beginning of the left subarray to the begin stack
				self.algo.begin.push(temp_begin)

				#push the end of the left subarray to the end stack
				self.algo.end.push(self.algo.i)

				#j = begin of left subarray
				self.algo.j=self.algo.begin.top()
				
				#i = begin-1 of left subarray
				self.algo.i=self.algo.begin.top()-1

				#pivot = end of left subarray
				self.algo.p=self.algo.end.top() #user could probably decide how pivot is chosen
		
		#if the subarray is sorted		
		else:
			
			#pop the top off of begin stack
			self.algo.begin.pop()

			#pop the top off of end stack
			self.algo.end.pop()

			#if the stacks are empty, then the entire array is sorted
			if(self.algo.begin.isEmpty()):

				self.algo.j-=1 #array[j] will be out of range without this line
				self.complete=True #sort is complete

			#if there are more subarrays to sort
			else:
				#set i, j, and pivot values
				self.algo.j=self.algo.begin.top()
				self.algo.i=self.algo.begin.top()-1
				self.algo.p=self.algo.end.top()

		

	#*****************************************************************************************
	#STEP ONCE	
	def step(self):

                #if sort is not complete, then step
		if(not self.complete):		
			
			#self.algo is an instance of InsertionSort
			if(isinstance(self.algo, InsertionStatus)):
				self.iterateInsertionSort()

			elif(isinstance(self.algo, QuickSortStatus)):
				self.iterateQuickSort()
				
                	#TODO: elifs for the other algorithms go here
		



################################################################################
# Used for testing and formatting of command line output                       #
################################################################################

if __name__ == '__main__':

        #creates algorithm obj
	x=Algorithm()

	#while algorithm is not complete, keep on steppin'
	while(not x.complete):

		#step it up!
		x.step()

		#local variables for i, j, and any others
		i = x.algo.i
		j = x.algo.j if x.algo.j<x.data.length-1 else x.algo.j-1
		b = 0 if x.algo.begin.isEmpty() else x.algo.begin.top()
		e = (x.data.length-1) if x.algo.end.isEmpty() else x.algo.end.top()
		
		#modularize output string

		#THIS FORMAT IS USED FOR QUICKSORT
		element_i = '\x1b[0;37;41m' + str(x.data.numbers[i]) + '\x1b[0m'
		element_j = '\x1b[0;30;44m' + str(x.data.numbers[j]) + '\x1b[0m'
		sortedData=str(x.data.numbers[:b])
		subArray = '\x1b[1;32m' + str(x.data.numbers[b:i]) + '\x1b[0m' + element_i + '\x1b[1;32m' + str(x.data.numbers[i+1:j]) + '\x1b[0m' + element_j + '\x1b[1;32m' + str(x.data.numbers[j+1:e]) + '\x1b[0m'
		unsortedData=str(x.data.numbers[e:])
		output="Data:\n"+sortedData+subArray+unsortedData+"\ni: "+str(i)+"\nj: "+str(j)


		#format the output string. the "\x1b[--m" values are for colors
		#THIS FORMAT IS USED FOR INSERTION SORT
		#output="Data:\n" + str(x.data.numbers[:j]) + '\x1b[0;37;41m' + str(x.data.numbers[j]) + '\x1b[0m' + str(x.data.numbers[j+1:i]) + '\x1b[0;30;44m' + str(x.data.numbers[i]) + '\x1b[0m' + str(x.data.numbers[i+1:]) +"\nj: " + str(x.algo.j) +"\ni: " + str(x.algo.i)
		

		#clear stdout
		os.system('clear')

		#print to cmdline
		print(output)

		#uncomment the following to wait for input for each step:
		#raw_input("<hit enter to step>")

		#wait for a bit so that the output can actually be seen
		time.sleep(.05)

	#One last print to check and make sure the above output is correct.
	print("\nReal, Unformatted Array:\n")
	print(x.data.numbers)
