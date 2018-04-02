class HeapSort(object):

	def __init__(self, StateObj):
		self.firstStep=True
		self.status=StateObj
		self.status.i=self.status.data.length//2-1
		self.lines=[]
		self.lines.append("def heapify(array, index, heap_size):")
		self.lines.append("\n\tlargest = index\n\tleft_index = 2 * index + 1\n\tright_index = 2 * index + 2")
		self.lines.append("\n\tif left_index < heap_size and array[left_index] > array[largest]:\n\t\tlargest = left_index\n\tif right_index < heap_size and array[right_index] > array[largest]:\n\t\tlargest = right_index\n\tif largest != index:\n\t\tarray[largest], array[index] = array[index], array[largest]\n\t\theapify(array, largest, heap_size)")
		self.lines.append("\n")
		self.lines.append("\ndef heapsort(array):")
		self.lines.append("\n\tn = len(array)")
		self.lines.append("\n\tfor i in range(n // 2 - 1, -1, -1):\n\t\theapify(array, i, n)")
		self.lines.append("\n\tfor j in range(n - 1, 0, -1):\n\t\tarray[0], array[j] = array[j], array[0]\n\t\theapify(array, 0, j)")
		self.lines.append("\n\treturn array")


	def iterate(self):

		#reset the initial values just in case sorting array was changed before 
		#the first step
		if(self.firstStep):
			self.firstStep=False
			self.status.i=self.status.data.length//2-1
			self.status.j=self.status.data.length-1
			self.largest=self.status.i
			self.left_index=2*self.status.i+1
			self.right_index=2*self.status.i+2
			self.do_iteration=True
			self.status.currentLine=9
			return

		#first for-loop
		if(self.status.i>=0):

			#this construction is basically like a toggle
			#for doing a recursive heapify versus a for-loop heapify
			if(self.do_iteration):
				self.index=self.status.i
			else:
				self.index=self.largest


			#set some variables
			self.largest=self.index
			self.left_index=2*self.index+1
			self.right_index=2*self.index+2
			self.status.compares+=3


			#if left_index<size and array[left_index]>array[largest]
			if(self.left_index < self.status.data.length and self.status.data.numbers[self.left_index] > self.status.data.numbers[self.largest]):
				self.largest=self.left_index

			#if right_index<size and array[right_index]>array[largest]
			if(self.right_index < self.status.data.length and self.status.data.numbers[self.right_index] > self.status.data.numbers[self.largest]):
				self.largest=self.right_index
			
			#if largest!=index	
			if(self.largest != self.index):
				#swap array[largest] and array[index]
				self.status.data.numbers[self.largest], self.status.data.numbers[self.index] = self.status.data.numbers[self.index], self.status.data.numbers[self.largest]

				#increment data movements
				self.status.swaps+=1
			
				#this is basically "heapify(array, largest, size)"
				self.do_iteration=False

				#set current pseudocode line
				self.status.currentLine=2

			#if largest==index
			else:

				#go back to the for-loop and decrement i
				self.do_iteration=True
				self.status.i-=1

				#set pseudocode line
				self.status.currentLine=6



		#second for-loop
		elif(self.status.j>0):

			#this construction is basically like a toggle
			#for doing a recursive heapify versus a for-loop heapify
			if(self.do_iteration):
				self.status.data.numbers[0], self.status.data.numbers[self.status.j] = self.status.data.numbers[self.status.j], self.status.data.numbers[0]
				self.index=0
				self.status.swaps+=1
			else:
				self.index=self.largest


			#set some variable values			
			self.largest=self.index
			self.left_index=2*self.index+1
			self.right_index=2*self.index+2
			self.status.compares+=3
		
			#if left_index<size and array[left_index]>array[largest]
			#size=j for this loop
			if(self.left_index < self.status.j and self.status.data.numbers[self.left_index] > self.status.data.numbers[self.largest]):
				self.largest=self.left_index

			#if right_index<size and array[right_index]>array[largest]
			#size=j for this loop
			if(self.right_index < self.status.j and self.status.data.numbers[self.right_index] > self.status.data.numbers[self.largest]):
				self.largest=self.right_index

			#if largest!=index
			if(self.largest != self.index):

				#swap array[largest] and array[index]
				self.status.data.numbers[self.largest], self.status.data.numbers[self.index] = self.status.data.numbers[self.index], self.status.data.numbers[self.largest]

				#increment data movements
				self.status.swaps+=1

				#set the pseudocode line
				self.status.currentLine=2

				#toggle the recursive heapify call
				self.do_iteration=False

			#if largest==index
			else:

				#set the pseudocode line
				self.status.currentLine=7

				#decrement j and go back to the for-loop
				self.do_iteration=True
				self.status.j-=1

		#sort is done
		else:
			self.status.sorting=False
			self.status.currentLine=8
			self.status.i=0
			self.status.j=1
