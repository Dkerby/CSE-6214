


class QuickSort(object):
	"""
	Pure implementation of quick sort algorithm in Python

	ARRAY_LENGTH = len(ARRAY)
	if( ARRAY_LENGTH <= 1):
		return ARRAY
	else:
		PIVOT = ARRAY[0]
		GREATER = [ element for element in ARRAY[1:] if element > PIVOT ]
		LESSER = [ element for element in ARRAY[1:] if element <= PIVOT ]
		return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)
    	"""
	def __init__(self, StateObj):
		self.status=StateObj
		self.status.i=-1
		self.status.j=0

		#these are stacks so that the algorithm can hold a trace/history
		#of the subarrays.
		self.begin=[0]
		self.end=[(len(self.status.data.numbers)-1)]

		#pivot defaults to last element of subarray
		self.p=(len(self.status.data.numbers)-1)


	def iterate(self):
		
		#if the subarray is not sorted
		if(self.top(self.begin)<self.top(self.end)):

			#if j is not at the end of the subarray
			if(self.status.j<self.top(self.end)):

				#if array[j] <= array[pivot]
				if(self.status.data.numbers[self.status.j]<=self.status.data.numbers[self.p]):
					
					#i++
					self.status.i+=1

					#swap array[i] and array[j]
					temp=self.status.data.numbers[self.status.j]
					self.status.data.numbers[self.status.j]=self.status.data.numbers[self.status.i]
					self.status.data.numbers[self.status.i]=temp

					#swaps++
					self.status.swaps+=1

				#j++
				self.status.j+=1

				#compares++
				self.status.compares+=1

			#if j has iterated through the subarray
			else:
				
				#swap array[i+1] and array[pivot]
				temp=self.status.data.numbers[(self.status.i+1)]
				self.status.data.numbers[(self.status.i+1)]=self.status.data.numbers[self.top(self.end)]
				self.status.data.numbers[self.top(self.end)]=temp

				#pop top of begin stack
				temp_begin=self.begin.pop()

				#append the beginning of the right subarray to the begin stack
				self.begin.append(self.status.i+2)

				#append the beginning of the left subarray to the begin stack
				self.begin.append(temp_begin)

				#append the end of the left subarray to the end stack
				self.end.append(self.status.i)

				#j = begin of left subarray
				self.status.j=self.top(self.begin)
				
				#i = begin-1 of left subarray
				self.status.i=self.top(self.begin)-1

				#pivot = end of left subarray
				self.p=self.top(self.end) #user could probably decide how pivot is chosen

				#swaps++
				self.status.swaps+=1
		
		#if the subarray is sorted		
		else:
			
			#pop the top off of begin stack
			self.begin.pop()

			#pop the top off of end stack
			self.end.pop()

			#if the stacks are empty, then the entire array is sorted
			if(self.begin==[]):

				self.status.j=0 
				self.status.i=1
				self.status.sorting=False #sort is complete

			#if there are more subarrays to sort
			else:
				#set i, j, and pivot values
				self.status.j=self.top(self.begin)
				self.status.i=self.top(self.begin)-1
				self.p=self.top(self.end)

	def top(self, arr):
		return arr[len(arr)-1]
