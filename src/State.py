class State():
    def __init__(self, NumberObj,sorting = False,speed=0.05):

        self.data=NumberObj
        self.sorting = sorting
        self.speed=float(speed)

        #the rest of the data members start at zero.
        #adjust manually to change them.
        self.currentLine = 0
        self.compares = 0
        self.swaps = 0
        self.memUsage = float(0.0)
        self.runtime = float(0.0)
        self.i=0
        self.j=0
        
        # def dump(self):
        #     print("x:", self.x)
        #     print("y:", self.y)
        #     print("y:", self.z)

        # def set_values(self,A,B,C):
        #     self.x = A
        #     self.y= B
        #     self.z= C
