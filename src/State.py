class State():
    def __init__(self, NumberObj,sorting = False,speed=0.05):

        self.data=NumberObj
        self.sorting = sorting
        self.benchmarking=True
        self.speed=float(speed)

        #the rest of the data members start at zero.
        #adjust manually to change them.
        self.currentLine = 0
        self.compares = 0
        self.swaps = 0
        self.memUsage = float(0.0)
        self.maxmem=float(0.0)
        self.runtime = float(0.0)
        self.i=0
        self.j=0
