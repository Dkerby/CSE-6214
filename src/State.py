class State():
    def __init__(self, currentLine = 0,sorting = False,comparisons = 0, movements = 0, memoryUsage = 0.0, runtime = 0.0):
        self.currentLine = int(currentLine)
        self.sorting = sorting
        self.comparisons = int(comparisons)
        self.movements = int(movements)
        self.memoryUsage = float(memoryUsage)
        self.runtime = float(runtime)
    
    # def dump(self):
    #     print("x:", self.x)
    #     print("y:", self.y)
    #     print("y:", self.z)

    # def set_values(self,A,B,C):
    #     self.x = A
    #     self.y= B
    #     self.z= C
