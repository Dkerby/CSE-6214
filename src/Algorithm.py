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
	def bottom(self):
		return self.items[0]

	def size(self):
		return len(self.items)
	
	#Outputs contents of entire stack. Used for testing.
	def __str__(self):
		retval=""
		for item in self.items:
			retval +=  str(item) + "\n"
		return retval

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

#Merge Sort Data
class MergeSortStatus(object):
	
	def __init__(self, data):
		self.i=0
		self.j=0
		self.real_i=0
		self.real_j=0
		self.SplitStack=Stack([data.numbers])
		self.MergeStack=Stack()
		self.mergeArray=[]



################################################################################
# THE MAIN ALGORITHM CLASS -- implements the stepping and sorting for each     #
# algorithm and also holds State and NumberList objects                        #
################################################################################

class Algorithm(object):

	#*****************************************************************************************
	#CONSTRUCTOR

	def __init__(self):
		self.data=nl.NumberList()#Create the NumberList obj
		self.data.generateRandom(24) #populates NumberList with random data. Used for testing...
		self.algo=MergeSortStatus(self.data) #Holds InsertionSort's information
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
	#MERGE SORT (this one was a real pain in the ass)

	def iterateMergeSort(self):

		#an abstraction to reduce complexity
		splitStack=self.algo.SplitStack
		mergeStack=self.algo.MergeStack
		mergeArray=self.algo.mergeArray
		merging=False
		
		


		# This algorithm has 2 segments: Splitting and Merging.
		#
		# Splitting does a split of the top array on the Split Stack
		# Merging combines the top two arrays on the Merge Stack
		#
		# first the algorithm checks to see if it can merge the top two
		# arrays on the mergeStack, and if it can, then it does. The algorithm should
		# NOT be able to split while it is merging (errors will happen).
		#
		# If the algorithm cant merge the top two arrays on the merge stack, then
		# it will split the arrays on the split stack until more can be added to the
		# merge stack

 		
		#the following elif statements check the top of the stack
		#if the stack is empty, top() will throw an error
		if(mergeStack.isEmpty()):
			merging=False #python also throws an error if theres no code in this block

		
		#If there is more than one array in the merge stack,
		#then check to see if they can merge
		elif((mergeStack.size() > 1) and (len(mergeStack.top()) < self.data.length)):

			#the righthalf of the merged array is the top of the stack
			righthalf=mergeStack.pop()

			#the lefthalf of the merged array is one below the top of the stack
			lefthalf=mergeStack.top()
			mergeStack.push(righthalf)

			#if the top two arrays on the merge stack have arrays that differ
			#by one or less in length, then they can merge.
			diff=len(lefthalf)-len(righthalf)
			if(diff<=1):

				#while merging, dont split the splitstack any more
				#(This is to prevent merging things out of order)
				merging=True

				#this is the actual merging algorithm
				if( self.algo.i < len(lefthalf) and self.algo.j<len(righthalf) ):
					if( lefthalf[self.algo.i] < righthalf[self.algo.j]):
						mergeArray.append(lefthalf[self.algo.i])
						self.algo.i+=1
					else:
						mergeArray.append(righthalf[self.algo.j])
						self.algo.j+=1

				elif( self.algo.i < len(lefthalf)):
					mergeArray.append(lefthalf[self.algo.i])
					self.algo.i+=1

				elif( self.algo.j < len(righthalf)):
					mergeArray.append(righthalf[self.algo.j])
					self.algo.j+=1


				#If the arrays are fully merged
				else:
					#reset i, j, and k
					self.algo.i=0
					self.algo.j=0
	
					#pop off the two arrays that were just merged
					mergeStack.pop()
					mergeStack.pop()

					#push the merged array
					mergeStack.push(mergeArray)
	
					#reset the array used for merging
					self.algo.mergeArray=[]
		
		#if sort is complete
		elif(len(mergeStack.top())==self.data.length):
			#self.data.numbers=mergeStack.top()
			self.complete=True

		if(not merging):

			#if the split stack is empty, dont do anything here
			if(splitStack.isEmpty()):
				return

			#split the array if the one one top has more than one
			elif(len(splitStack.top()) > 1):

				#pop it off
				temp=splitStack.pop()

				#divide it in half and push the two halfs back on the stack
				mid=(len(temp)/2)
				splitStack.push(temp[:mid])
				splitStack.push(temp[mid:])
		
			#if the top array on the splitStack is exactly one element
			else:
				#pop it off the split stack and push it on the merge stack
				while(len(splitStack.top())==1):
					mergeStack.push(splitStack.pop())
					if(splitStack.isEmpty()):
						return
		self.updateMergeArray()

	
	#this method updates self.data to reflect what is actually happening
	#to the subarrays
	#it also calculates the real i and j values relative to the whole array.
	#self.i and self.j are normally only the i and j values relative to the subarray.
	def updateMergeArray(self):
	
		#indirection for reduced complexity
		mergestack=self.algo.MergeStack
		splitstack=self.algo.SplitStack
		i=self.algo.i
		j=self.algo.j

		#our temporary "true" array variable
		newArray=[]
	
		#i and j start at 0
		self.algo.real_i=0
		self.algo.real_j=0

		#for each array in the stack
		for item in mergestack.items:
	
			#add the elements of the array to newArray
			newArray+=item

			#increment i and j
			self.algo.real_i+=len(item)
			self.algo.real_j+=len(item)

		#for each array in the stack
		for item in splitstack.items:	
			#add the elements of the array to newArray
			newArray+=item

		#if the mergestack is empty, i and j are zero
		if(not mergestack.isEmpty()):

			#if the mergestack has 2 or more arrays
			if(mergestack.size()>1):

				#holds top element so that we can get the array below the top
				temp=mergestack.pop()

				#reduce i and j by the size of the array on top
				self.algo.real_j-= len(temp)
				self.algo.real_i-= len(temp)
	
				#reduce i by the size of the second array from the top
				self.algo.real_i-= len(mergestack.top())
			
				#put this back on the stack, because we are done using it
				mergestack.push(temp)
		
				#real i and j are now at the start of their respective subarrays
				#so add the relative i and j values to them
				self.algo.real_i+=i
				self.algo.real_j+=j


			#if there is one array on the stack, then we are not merging
			#and i and j should just be 0
			elif(mergestack.size()==1):
				self.algo.real_i=0
				self.algo.real_j=0	
	
		#if the stack is empty, i and j are zero
		else:	
			self.algo.real_i=0
			self.algo.real_j=0

		#update self.data.numbers
		self.data.numbers=newArray

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
				
                	
			elif(isinstance(self.algo, MergeSortStatus)):
				self.iterateMergeSort()			
				
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
		i = x.algo.i if x.algo.i<x.data.length-1 else x.algo.i-1
		j = x.algo.j if x.algo.j<x.data.length-1 else x.algo.j-1
		#b = 0 if x.algo.begin.isEmpty() else x.algo.begin.top()
		#e = (x.data.length-1) if x.algo.end.isEmpty() else x.algo.end.top()
		
		#-----------------------FORMATTING--------------------------------#
		# \x1b[...m  values are for colors

		#THIS FORMAT IS USED FOR MERGESORT
		#formatting for mergesort is very different than the others
		#this might need some adjusting
		i=x.algo.real_i if x.algo.real_i<x.data.length-1 else x.algo.real_i-1
		j=x.algo.real_j if x.algo.real_j<x.data.length-1 else x.algo.real_j-1
		element_i = '\x1b[0;37;41m' + str(x.data.numbers[i]) + '\x1b[0m'
		element_j = '\x1b[0;30;44m' + str(x.data.numbers[j]) + '\x1b[0m'

		output="Unsorted Stack:\n\n" + str(x.algo.SplitStack) + "\n Merge Stack:\n\n" + str(x.algo.MergeStack)+ "\n\nDATA:\n\n"+ str(x.data.numbers[:i]) + element_i + str(x.data.numbers[i+1:j]) + element_j + str(x.data.numbers[j+1:])+"\n\ni: " + str(i) + "\nj: " + str(j)

		#THIS FORMAT IS USED FOR QUICKSORT
		#b = 0 if x.algo.begin.isEmpty() else x.algo.begin.top()
		#e = (x.data.length-1) if x.algo.end.isEmpty() else x.algo.end.top()
		#element_i = '\x1b[0;37;41m' + str(x.data.numbers[i]) + '\x1b[0m'
		#element_j = '\x1b[0;30;44m' + str(x.data.numbers[j]) + '\x1b[0m'
		#sortedData=str(x.data.numbers[:b])
		#subArray = '\x1b[1;32m' + str(x.data.numbers[b:i]) + '\x1b[0m' + element_i + '\x1b[1;32m' + str(x.data.numbers[i+1:j]) + '\x1b[0m' + element_j + '\x1b[1;32m' + str(x.data.numbers[j+1:e]) + '\x1b[0m'
		#unsortedData=str(x.data.numbers[e:])
		#output="Data:\n"+sortedData+subArray+unsortedData+"\ni: "+str(i)+"\nj: "+str(j)


		#THIS FORMAT IS USED FOR INSERTION SORT
		#output="Data:\n" + str(x.data.numbers[:j]) + '\x1b[0;37;41m' + str(x.data.numbers[j]) + '\x1b[0m' + str(x.data.numbers[j+1:i]) + '\x1b[0;30;44m' + str(x.data.numbers[i]) + '\x1b[0m' + str(x.data.numbers[i+1:]) +"\nj: " + str(x.algo.j) +"\ni: " + str(x.algo.i)
		

		#clear stdout
		os.system('clear')

		#print to cmdline
		print(output)

		#uncomment the following to wait for input for each step:
		raw_input("<hit enter to step>")

		#wait for a bit so that the output can actually be seen
		time.sleep(.05)

	#One last print to check and make sure the above output is correct.
	print("\nReal, Unformatted Array:\n")
	print(x.data.numbers)
