
class InsertionSort(object):
	"""
	Pure implementation of the insertion sort algorithm in Python

	for index in range(1, len(array)):
		while 0 < index and array[index] < array[index - 1]:
			array[index], array[index - 1] = array[index - 1], array[index]
			index -= 1

	return array
	"""
	def __init__(self, StateObj):
		self.status=StateObj
		self.status.i=1
		self.status.j=1
		self.cval=self.status.data.numbers[self.status.i]

	def iterate(self):
		
		# if ( j > 0 && array[j-1] > cval ):
		if(self.status.j>0 and self.status.data.numbers[self.status.j-1]>self.cval):

                        # array[j]=array[j-1]
			self.status.data.numbers[self.status.j]=self.status.data.numbers[self.status.j-1]

			# j--
			self.status.j-=1

			#swaps++
			#compares++
			self.status.compares+=1
			self.status.swaps+=1
		else:

                        # array[j] = cval
			self.status.data.numbers[self.status.j]=self.cval

			# i++
			self.status.i+=1
	
			#compares++
			self.status.compares+=1

			# if ( i < len(array) )
			if(self.status.i<self.status.data.length):

                                # cval = array[i]
				self.cval=self.status.data.numbers[self.status.i]

				# j = i
				self.status.j=self.status.i

			else:

				# set i and j to 0
				self.status.i=0
				self.status.j=0

				# sort is complete
				self.status.sorting=False
