


class QuickSort(object):
	"""
	Pure implementation of quick sort algorithm in Python


	if( len(array) <= 1):
		return
	else:
		pivot = len(array)-1
		i=0
		for j in array:
			if j <= array[pivot]:
				i++
				array[i], j = j, array[i]
		array[i+1], array[pivot] = array[pivot], array[i+1]
		QuickSort(array[:i+1])
		QuickSort(array[i+2:])
				
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

		self.lines=[]
		self.lines.append("\nif( len(array) <= 1):\n\treturn")
		self.lines.append("\nelse:\n\tpivot = len(array)-1\n\ti=0")
		self.lines.append("\n\tfor j in array:")
		self.lines.append("\n\t\tif j <= array[pivot]:")
		self.lines.append("\n\t\t\ti++\n\t\t\tarray[i], j = j, array[i]")
		self.lines.append("\n\tarray[i+1], array[pivot] = array[pivot], array[i+1]")
		self.lines.append("\n\tQuickSort(array[:i+1])\n\tQuickSort(array[i+2:])")


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

					self.status.currentLine=4
	
				else:
					self.status.currentLine=3

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

				self.status.currentLine=6
		
		#if the subarray is sorted		
		else:
			
			#pop the top off of begin stack
			self.begin.pop()

			#pop the top off of end stack
			self.end.pop()

			self.status.currentLine=0

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
