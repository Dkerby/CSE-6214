
class BubbleSort(object):
	"""
	Pure implementation of bubble sort algorithm in Python

	length = len(array)
	for i in range(length):
		for j in range(length-1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]

	return array
	"""

	def __init__(self, StateObj):
		self.status=StateObj
		self.lines=[]
		self.lines.append("\nfor i in range(len(array)):")
		self.lines.append("\n\tfor j in range(len(array)-1):")
		self.lines.append("\n\t\tif array[j] > [j+1]:")
		self.lines.append("\n\t\t\tarray[j], array[j+1] = array[j+1], array[j]")


	def iterate(self):
		
		arrLength=self.status.data.length
		if(self.status.i<arrLength):

			if(self.status.j<(arrLength-self.status.i-1)):
				if(self.status.data.numbers[self.status.j]>self.status.data.numbers[self.status.j+1]):
					self.status.data.numbers[self.status.j], self.status.data.numbers[self.status.j+1] = self.status.data.numbers[self.status.j+1], self.status.data.numbers[self.status.j]
					
					#swaps++
					#compares++
					self.status.compares+=1
					self.status.swaps+=1

					self.status.currentLine=3
				else:
					self.status.currentLine=2

				self.status.j+=1

				#compares++
				self.status.compares+=1

			else:
				self.status.j=0
				self.status.i+=1
				self.status.currentLine=1
		else:
			self.status.i=0
			self.status.j=0
			self.status.sorting=False
			self.status.currentLine=0


