from __future__ import print_function
from sortlib import bubble_sort, insertion_sort, quick_sort, merge_sort, heap_sort
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
                self.benchindex=0
                self.cachefile="sortcache.txt"
                self.outputfile=""

                #switchcase for algorithm choice
                if(algo==1):
                        self.algo=insertion_sort.InsertionSort(self.status)
                elif(algo==2):
                        self.algo=bubble_sort.BubbleSort(self.status)
                elif(algo==3):
                        self.algo=quick_sort.QuickSort(self.status)
                elif(algo==4):
                        self.algo=merge_sort.MergeSort(self.status)
                elif(algo==5):
                        self.algo=heap_sort.HeapSort(self.status)



        #*****************************************************************************************
        # RESET THE SORT
        def reset(self, algo=0):

                #reset state
                length=self.status.data.length
                self.status=st.State(nl.NumberList(),True, self.status.speed)
                self.status.data.generateRandom(length)

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
                elif(algo==5):
                        self.algo=heap_sort.HeapSort(self.status)


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
        # void importData(string filename)
        def importData(self,filename):
                self.status.data.importListFromFile(filename)

        #*****************************************************************************************
        # void importText(string filename)      
        def importText(self, filetext):
                self.status.data.importListFromText(filetext)
        
        #*****************************************************************************************
        # void exportData(string filename)
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
                if(i<0):
                        i=0
                if(j<0):
                        j=0
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

                #MERGE SORT FORMATTING  
                elif(self.algochoice==5):
                        element_i = '\x1b[0;37;41m' + str(self.status.data.numbers[i]) + '\x1b[0m'
                        element_j = '\x1b[0;30;44m' + str(self.status.data.numbers[j]) + '\x1b[0m'

                        output="DATA:\n\n"+ str(self.status.data.numbers[:i]) + element_i + str(self.status.data.numbers[i+1:j]) + element_j + str(self.status.data.numbers[j+1:])


                else:
                        output=str(self.getData())

                return output
                        

        #*****************************************************************************************
        # STEP ONCE     
        def step(self):

                #if sort is not complete, then step
                if(self.status.sorting):                
                        
                        #self.algo is an instance of whatever sorting algorithm we're using's class
                        initialtime=time.time()
                        self.algo.iterate()
                        snapshot=tracemalloc.take_snapshot()
                        filters=[tracemalloc.Filter(True, "*sort.py")]
                        filtered_snap=snapshot.filter_traces(filters)
                        stats=filtered_snap.statistics('filename')
                        self.status.memUsage=stats[0].size
                        if(self.status.maxmem<self.status.memUsage):
                                self.status.maxmem=self.status.memUsage
                        time.sleep(self.status.speed)
                        deltatime=time.time() - initialtime
                        self.status.runtime+=deltatime




        #*****************************************************************************************
        # SETUP THE ALGORITHM OBJECT FOR BENCHMARKING
        
        def benchsetup(self, randsize=200, inputfile="", outputfile="benchmark.log"):

                #set outputfile
                self.outputfile=outputfile

                #if user wants to import a file with data, this will allow it
                if(inputfile!=""):
                        self.importData(inputfile)

                else:
                        self.setRandomData(randsize)


                #keep unsorted data in the cachefile so the sorts can be reset
                self.exportData(self.cachefile)

                #output the inital unsorted array to the outputfile
                of=open(self.outputfile,"w")
                of.write("Initial Data: \n")

                first=True
                for num in self.status.data.numbers:
                        if(first):
                                of.write(str(num))
                                first=False
                        else:
                                of.write(', ' + str(num))
                                
                of.write("\n\n")
                of.close()

                #set benchmark index to 1. this starts it at algochoice=1
                self.benchindex=1


        #*****************************************************************************************
        # BENCHMARK STEP ONCE
        
        def benchstep(self):
                
                #do each sort, one after another
                if(self.status.sorting):

                        #step if the sort is in progress
                        self.step()

                #if the individual sort is not in progress
                else:

                        #if there are still more individual sorts to do
                        if(self.benchindex<5):

                                #output metadata to outputfile
                                of=open(self.outputfile,"a")
                                of.write("Sort Used: \t\t")
                                if(self.algochoice==1):
                                        of.write("Insertion Sort\n")
                                elif(self.algochoice==2):
                                        of.write("Bubble Sort\n")
                                elif(self.algochoice==3):
                                        of.write("Quick Sort\n")
                                elif(self.algochoice==4):
                                        of.write("Merge Sort\n")
                                elif(self.algochoice==5):
                                        of.write("Heap Sort\n")
                                else:
                                        of.write("Unknown\n")

                                of.write("Data Movements: \t" + str(self.status.swaps) + "\n")
                                of.write("Data Comparisons: \t" + str(self.status.compares) + "\n")
                                of.write("Memory Used: \t\t" + str(self.status.maxmem) + " Bytes\n")
                                of.write("Runtime: \t\t"+str("{0:.2f}".format(self.status.runtime))+" Seconds\n")
                                of.write("\n")
                                of.close()

                                #increment benchindex
                                self.benchindex+=1

                                #reset the sort
                                self.reset(self.benchindex)

                                #import unsorted data from cachefile
                                self.importData(self.cachefile)

                                

                        #if the benchmark has done each algorithm
                        else:

                                #output the last sorts metadata to outputfile
                                of=open(self.outputfile,"a")
                                of.write("Sort Used: \t\t")
                                if(self.algochoice==1):
                                        of.write("Insertion Sort\n")
                                elif(self.algochoice==2):
                                        of.write("Bubble Sort\n")
                                elif(self.algochoice==3):
                                        of.write("Quick Sort\n")
                                elif(self.algochoice==4):
                                        of.write("Merge Sort\n")
                                elif(self.algochoice==5):
                                        of.write("Heap Sort\n")
                                else:
                                        of.write("Unknown\n")

                                of.write("Data Movements: \t" + str(self.status.swaps) + "\n")
                                of.write("Data Comparisons: \t" + str(self.status.compares) + "\n")
                                of.write("Memory Used: \t\t" + str(self.status.maxmem) + " Bytes\n")
                                of.write("Runtime: \t\t"+str("{0:.2f}".format(self.status.runtime))+" Seconds\n")
                                of.write("\n")

                                #output the sorted data to outputfile to make
                                #sure that the data sorted correctly
                                of.write("\nSorted Data: \n")
                                first=True
                                for num in self.status.data.numbers:
                                        if(first):
                                                of.write(str(num))
                                                first=False
                                        else:
                                                of.write(', ' + str(num))

                                of.close()

                                #stop benchmarking
                                self.status.benchmarking=False

