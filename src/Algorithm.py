from __future__ import print_function
from sortlib import bubble_sort, insertion_sort, quick_sort, merge_sort
import tracemalloc



################################################################################
# THE MAIN ALGORITHM CLASS -- implements the stepping and sorting for each     #
# algorithm and also holds State and NumberList objects                        #
################################################################################

class Algorithm(object):

        #*****************************************************************************************
        # CONSTRUCTOR

        def __init__(self, StateObj, algo=1):

                #start tracing memory for this sort
                tracemalloc.start(25)
                
                #set status for algorithm
                self.status=StateObj

                #holds the choice of algorithm
                self.algochoice=algo

                #switchcase for algorithm choice
                if(algo==1):
                        self.algo=insertion_sort.InsertionSort(self.status)
                elif(algo==2):
                        self.algo=bubble_sort.BubbleSort(self.status)
                elif(algo==3):
                        self.algo=quick_sort.QuickSort(self.status)
                elif(algo==4):
                        self.algo=merge_sort.MergeSort(self.status)



        #*****************************************************************************************
        # RESET THE SORT
        def reset(self, NumberObj=None, algo=0, reset_mem=True, reset_runtime=True):
                
                if(NumberObj==None):
                        NumberObj=self.status.data.generateRandom(self.status.data.length)
                #restarts algorithm from the beginning with new set of data
                self.status.currentLine=0
                self.status.swaps=0
                self.status.compares=0
                self.status.sorting=True
                self.status.data=NumberObj

                #option for resetting memory usage
                if(reset_mem):
                        self.status.memUsage=0.0

                #option for resetting runtime
                if(reset_runtime):
                        self.status.runtime=0.0

                #holds potentially new algochoice
                if(algo!=0):
                        self.algochoice=algo
                else:
                        algo=self.algochoice


                #switchcase for algorithm choice
                if(algo==1):
                        self.algo=insertion_sort.InsertionSort(self.status)
                elif(algo==2):
                        self.algo=bubble_sort.BubbleSort(self.status)
                elif(algo==3):
                        self.algo=quick_sort.QuickSort(self.status)
                elif(algo==4):
                        self.algo=merge_sort.MergeSort(self.status)


        #*****************************************************************************************
        # STEP ONCE     
        def step(self):

                #if sort is not complete, then step
                if(self.status.sorting):                
                        
                        #self.algo is an instance of whatever sorting algorithm we're using's class
                        self.algo.iterate()
                        snapshot=tracemalloc.take_snapshot()
                        filters=[tracemalloc.Filter(True, "*sort.py")]
                        filtered_snap=snapshot.filter_traces(filters)
                        stats=filtered_snap.statistics('filename')
                        self.status.memUsage=stats[0].size
                

