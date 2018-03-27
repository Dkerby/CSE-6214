from __future__ import print_function
from sortlib import bubble_sort, insertion_sort, quick_sort, merge_sort
import tracemalloc
import State as st #holds state of algorithm
import NumberList as nl #holds the data
import time




################################################################################
# THE MAIN ALGORITHM CLASS -- implements the stepping and sorting for each     #
# algorithm and also holds State and NumberList objects                        #
################################################################################

class Algorithm(object):

        #*****************************************************************************************
        # CONSTRUCTOR

        def __init__(self, sorting=True, algo=1, speed=0.025, arrsize=200):

                #start tracing memory for this sort
                tracemalloc.start(25)
                #set status for algorithm
                self.status=st.State(nl.NumberList(), sorting, speed)
                self.status.data.generateRandom(arrsize)
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
        def reset(self, algo=0):

                #reset state
                length=self.status.data.length
                self.status=st.State(nl.NumberList(),True, self.status.speed)
                self.status.data.generateRandom(length)
                self.data.generateRandom(self.data.length)

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
        #dictionary getStatus(void)
        def getState(self):
                return self.status
        
        #*****************************************************************************************
        # void setData(int list)
        def setData(self, numbers=[]):
                self.status.data=nl.NumberList(numbers)
                
        #*****************************************************************************************
        # int list getData()
        def getData(self):
                return self.status.data.numbers
        
        #*****************************************************************************************
        # bool importData(string filename)
        def importData(self,filename):
                self.status.data.importListFromFile(filename)

        
        #*****************************************************************************************
        # bool exportData(string filename)
        def exportData(self,filename):
                self.status.data.exportListToFile(filename)
                
        #*****************************************************************************************
        # void setRandomData(size)
        def setRandomData(self,size):
                self.status.data.generateRandom(size)
                
        #*****************************************************************************************
        # string getFormat()
        def getFormat(self):
                i=self.status.i if self.status.i<self.status.data.length-1 else 0
                j=self.status.j if self.status.j<self.status.data.length-1 else 0
                #INSERTION SORT FORMATTING
                if(self.algochoice==1):
                        output=str(self.status.data.numbers[:j]) + '\x1b[0;37;41m' + str(self.status.data.numbers[j]) + '\x1b[0m' + str(self.status.data.numbers[j+1:i]) + '\x1b[0;30;44m' + str(self.status.data.numbers[i]) + '\x1b[0m' + str(self.status.data.numbers[i+1:])



                #QUICK SORT FORMATTING
                elif(self.algochoice==3):
                        b = 0 if self.algo.begin==[] else self.algo.top(self.algo.begin)
                        e = (self.status.data.length-1) if self.algo.end==[] else self.algo.top(self.algo.end)
                        element_i = '\x1b[0;37;41m' + str(self.status.data.numbers[i]) + '\x1b[0m'
                        element_j = '\x1b[0;30;44m' + str(self.status.data.numbers[j]) + '\x1b[0m'
                        sortedData=str(self.status.data.numbers[:b])
                        subArray = '\x1b[1;32m' + str(self.status.data.numbers[b:i]) + '\x1b[0m' + element_i + '\x1b[1;32m' + str(self.status.data.numbers[i+1:j]) + '\x1b[0m' + element_j + '\x1b[1;32m' + str(self.status.data.numbers[j+1:e]) + '\x1b[0m'
                        unsortedData=str(self.status.data.numbers[e:])
                        output=sortedData+subArray+unsortedData


                                
                #MERGE SORT FORMATTING  
                elif(self.algochoice==4):
                        element_i = '\x1b[0;37;41m' + str(self.status.data.numbers[i]) + '\x1b[0m'
                        element_j = '\x1b[0;30;44m' + str(self.status.data.numbers[j]) + '\x1b[0m'

                        output="Unsorted Stack:\n\n" + str(self.algo.splitStack) + "\n Merge Stack:\n\n" + str(self.algo.mergeStack)+ "\n\nDATA:\n\n"+ str(self.status.data.numbers[:i]) + element_i + str(self.status.data.numbers[i+1:j]) + element_j + str(self.status.data.numbers[j+1:])



                #BUBBLE SORT FORMATTING 
                elif(self.algochoice==2):
                        prehighlights=str(self.status.data.numbers[:j])
                        highlights= '\x1b[0;37;41m' + str(self.status.data.numbers[j]) + '\x1b[0m' + '\x1b[0;30;44m' + str(self.status.data.numbers[j+1]) + '\x1b[0m'
                        posthighlights=str(self.status.data.numbers[j+2:])
                        output=prehighlights + highlights + posthighlights

                else:
                        output=str(self.getData())

                return output
                        

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
                        time.sleep(self.status.speed)
                

