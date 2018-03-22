

#they should rename this one to 'pain-in-the-ass-sort'
class MergeSort(object):
	"""
	Pure implementation of the merge sort algorithm in Python

	length = len(array)
	if length > 1:
		midpoint = length // 2
		left_half = merge_sort(array[:midpoint])
		right_half = merge_sort(array[midpoint:])
		i = 0
		j = 0
		k = 0
		left_length = len(left_half)
		right_length = len(right_half)
		while i < left_length and j < right_length:
			if left_half[i] < right_half[j]:
				array[k] = left_half[i]
		        	i += 1
			else:
				array[k] = right_half[j]
				j += 1
			k += 1

		while i < left_length:
			array[k] = left_half[i]
			i += 1
			k += 1

		while j < right_length:
			array[k] = right_half[j]
			j += 1
			k += 1

	return array
	"""
	def __init__(self, StateObj):
		self.status=StateObj
		self.status.i=0
		self.status.j=0
		self.relative_i=0
		self.relative_j=0
		self.splitStack=[self.status.data.numbers]
		self.mergeStack=[]
		self.mergeArray=[]

	def iterate(self):

		#an abstraction to reduce complexity
		splitStack=self.splitStack
		mergeStack=self.mergeStack
		mergeArray=self.mergeArray
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
		if(mergeStack==[]):
			merging=False #python also throws an error if theres no code in this block

		
		#If there is more than one array in the merge stack,
		#then check to see if they can merge
		elif((len(mergeStack) > 1) and (len(self.top(mergeStack)) < self.status.data.length)):

			#the righthalf of the merged array is the top of the stack
			righthalf=mergeStack[len(mergeStack)-1]

			#the lefthalf of the merged array is one below the top of the stack
			lefthalf=mergeStack[len(mergeStack)-2]

			#if the top two arrays on the merge stack have arrays that differ
			#by one or less in length, then they can merge.
			diff=len(lefthalf)-len(righthalf)
			if(diff<=1):
				#compares++
				self.status.compares+=1

				#while merging, dont split the splitstack any more
				#(This is to prevent merging things out of order)
				merging=True

				#this is the actual merging algorithm
				if( self.relative_i < len(lefthalf) and self.relative_j<len(righthalf) ):

					if( lefthalf[self.relative_i] < righthalf[self.relative_j]):
						mergeArray.append(lefthalf[self.relative_i])
						self.relative_i+=1

						#swaps++
						self.status.swaps+=1
					else:
						mergeArray.append(righthalf[self.relative_j])
						self.relative_j+=1

						#swaps++
						self.status.swaps+=1

					#compares++
					self.status.compares+=1

				elif( self.relative_i < len(lefthalf)):
					mergeArray.append(lefthalf[self.relative_i])
					self.relative_i+=1
					
					#swaps++
					#compares++
					self.status.compares+=1
					self.status.swaps+=1

				elif( self.relative_j < len(righthalf)):
					mergeArray.append(righthalf[self.relative_j])
					self.relative_j+=1

					#swaps++
					#compares++
					self.status.compares+=1
					self.status.swaps+=1


				#If the arrays are fully merged
				else:
					#reset i, j
					self.relative_i=0
					self.relative_j=0
	
					#pop off the two arrays that were just merged
					self.mergeStack.pop()
					self.mergeStack.pop()

					#push the merged array
					self.mergeStack.append(mergeArray)
	
					#reset the array used for merging
					self.mergeArray=[]
		
		#if sort is complete
		elif(len(self.top(mergeStack))==self.status.data.length):
			#self.data.numbers=self.top(mergeStack)
			self.status.sorting=False

		if(not merging):

			#if the split stack is empty, dont do anything here
			if(splitStack==[]):
				return

			#split the array if the one one top has more than one
			elif(len(self.top(splitStack)) > 1):

				#pop it off
				temp=self.splitStack.pop()

				#divide it in half and push the two halfs back on the stack
				mid=(len(temp)/2)
				self.splitStack.append(temp[:mid])
				self.splitStack.append(temp[mid:])
		
			#if the top array on the splitStack is exactly one element
			else:
				#pop it off the split stack and push it on the merge stack
				while(len(self.top(splitStack))==1):

					self.mergeStack.append(self.splitStack.pop())
					if(self.splitStack==[]):
						return
		self.updateMergeArray()

	
	#this method updates self.data to reflect what is actually happening
	#to the subarrays
	#it also calculates the real i and j values relative to the whole array.
	#self.i and self.j are normally only the i and j values relative to the subarray.
	def updateMergeArray(self):
	
		#indirection for reduced complexity
		mergestack=self.mergeStack
		splitstack=self.splitStack
		i=self.relative_i
		j=self.relative_j

		#our temporary "true" array variable
		newArray=[]
	
		#i and j start at 0
		self.status.i=0
		self.status.j=0

		#for each array in the stack
		for item in mergestack:
	
			#add the elements of the array to newArray
			newArray+=item

			#increment i and j
			self.status.i+=len(item)
			self.status.j+=len(item)

		#for each array in the stack
		for item in splitstack:	
			#add the elements of the array to newArray
			newArray+=item

		#if the mergestack is empty, i and j are zero
		if(not mergestack==[]):

			#if the mergestack has 2 or more arrays
			if(len(mergestack)>1):

				#holds top element so that we can get the array below the top
				temp=self.top(mergestack)

				#reduce i and j by the size of the array on top
				self.status.j-= len(temp)
				self.status.i-= len(temp)
	
				#reduce i by the size of the second array from the top
				self.status.i-= len(mergestack[len(mergestack)-2])
		
				#real i and j are now at the start of their respective subarrays
				#so add the relative i and j values to them
				self.status.i+=i
				self.status.j+=j


			#if there is one array on the stack, then we are not merging
			#and i and j should just be 0
			elif(len(mergestack)==1):
				self.status.i=0
				self.status.j=0	
	
		#if the stack is empty, i and j are zero
		else:	
			self.status.i=0
			self.status.j=0

		#update self.data.numbers
		self.status.data.numbers=newArray

	def top(self, arr):
		return arr[len(arr)-1]


