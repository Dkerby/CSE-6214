from __future__ import print_function

import time,os,sys, getopt 
#time used for waiting, os used for clearing the cmdline output, 
#sys and geopt used for cmdline arguments

import NumberList as nl #holds the data
import State as st #holds state of algorithm
import Algorithm as alg # holds algorithm

################################################################################
# Used for testing and formatting of command line output                       #
################################################################################


#MAIN PROGRAM
def main(argv):

        #default values for the sort
        arrsize=200
        algochoice=1
        MAXARRAYSIZE=2048
        wait=False
        speed=0.05

        
        #parsing of command line options
        try:
                opts, args = getopt.getopt(argv,"hwr:a:s:",["randnum=", "algo=", "spd="])

        #error prints out the help info
        except getopt.GetoptError:
                print('\n\ttest.py\n\t[-r <size of array>]\n\t[-a <chosen algorithm (1-4)>]\n\t[-s <speed of algorithm>]')
                print('\n\t-h displays help info')
                print('\t-w toggles on the WAIT_FOR_USER step option\n')
                print('\t1 - Insertion Sort')
                print('\t2 - Bubble Sort')
                print('\t3 - Quick Sort')
                print('\t4 - Merge Sort')

                sys.exit(2)

        #for each option in the command line arguments
        for opt, arg in opts:

                # -h prints out help info
                if opt == '-h':
                        print('\n\ttest.py\n\t[-r <size of array>]\n\t[-a <chosen algorithm (1-4)>]\n\t[-s <speed of algorithm>]')
                        print('\n\t-h displays help info')
                        print('\t-w toggles on the WAIT_FOR_USER step option\n')
                        print('\t1 - Insertion Sort')
                        print('\t2 - Bubble Sort')
                        print('\t3 - Quick Sort')
                        print('\t4 - Merge Sort')
                        sys.exit()

                # -r lets user set the size of the randomly generated array
                elif opt in ("-r", "--randnum"):
                        arrsize = int(arg)

                # -a lets the user choose which algorithm they want to do
                elif opt in ("-a", "--algo"):
                        algochoice = int(arg)

                # -s lets the user set the speed of the stepping
                elif opt in ("-s", "--spd"):
                        speed=float(arg)

                # -w is a toggle on the <press enter to step> portion of the output
                elif opt =="-w":
                        wait=True
        

        #print error and exit if the user's options are silly
        if(arrsize<1 or arrsize>MAXARRAYSIZE):
                print("Array inappropriately sized.")
                sys.exit(2)
        if(algochoice<1 or algochoice>4):
                print("That is not one of the available algorithms")
                sys.exit(2)

        if(speed<0.0001 or speed>5.0):
                print("That is either too fast or too slow")
                sys.exit(2)

        print('Generating array of size', arrsize)
        print('Algorithm choice is ', algochoice)


        #creates NumberList, State, and Algorithm objects
        NumberObj=nl.NumberList() #empty at first
        NumberObj.generateRandom(arrsize) #generate array of size <arrsize>
        StateObj=st.State(NumberObj, True, speed) #create state object to hold status info
        x=alg.Algorithm(StateObj, algochoice) #pass State object into Algorithm along with the choice of algorithm

        #while algorithm is not complete, keep on steppin'
        while(StateObj.sorting):

                #step it up!
                x.step()

                #local variables for i, j, and any others
                #this ternary-operator-esque structure is to ensure we dont
                #try to look at an index that is out of bounds of the array
                i = StateObj.i if StateObj.i<NumberObj.length-1 else StateObj.i-1
                j = StateObj.j if StateObj.j<NumberObj.length-1 else StateObj.j-1


                
                #-----------------------FORMATTING--------------------------------#
                # This section formats the output for the algorithm that the user has
                # picked. most of the information is in the State object, but some of the
                # data members are specific to the algorithm. these specific data members
                # are in the specific algorithm class, which can be found by calling 
                # Algorithm.algo.[whatever value you want]
                #
                # \x1b[...m  values are for colors

                #INSERTION SORT FORMATTING
                if(x.algochoice==1):
                        output="Data:\n" + str(NumberObj.numbers[:j]) + '\x1b[0;37;41m' + str(NumberObj.numbers[j]) + '\x1b[0m' + str(NumberObj.numbers[j+1:i]) + '\x1b[0;30;44m' + str(NumberObj.numbers[i]) + '\x1b[0m' + str(NumberObj.numbers[i+1:])



                #QUICK SORT FORMATTING
                elif(x.algochoice==3):
                        b = 0 if x.algo.begin==[] else x.algo.top(x.algo.begin)
                        e = (NumberObj.length-1) if x.algo.end==[] else x.algo.top(x.algo.end)
                        element_i = '\x1b[0;37;41m' + str(NumberObj.numbers[i]) + '\x1b[0m'
                        element_j = '\x1b[0;30;44m' + str(NumberObj.numbers[j]) + '\x1b[0m'
                        sortedData=str(NumberObj.numbers[:b])
                        subArray = '\x1b[1;32m' + str(NumberObj.numbers[b:i]) + '\x1b[0m' + element_i + '\x1b[1;32m' + str(NumberObj.numbers[i+1:j]) + '\x1b[0m' + element_j + '\x1b[1;32m' + str(NumberObj.numbers[j+1:e]) + '\x1b[0m'
                        unsortedData=str(NumberObj.numbers[e:])
                        output="Data:\n"+sortedData+subArray+unsortedData


                                
                #MERGE SORT FORMATTING  
                elif(x.algochoice==4):
                        element_i = '\x1b[0;37;41m' + str(NumberObj.numbers[i]) + '\x1b[0m'
                        element_j = '\x1b[0;30;44m' + str(NumberObj.numbers[j]) + '\x1b[0m'

                        output="Unsorted Stack:\n\n" + str(x.algo.splitStack) + "\n Merge Stack:\n\n" + str(x.algo.mergeStack)+ "\n\nDATA:\n\n"+ str(NumberObj.numbers[:i]) + element_i + str(NumberObj.numbers[i+1:j]) + element_j + str(NumberObj.numbers[j+1:])



                #BUBBLE SORT FORMATTING 
                elif(x.algochoice==2):
                        prehighlights=str(NumberObj.numbers[:j])
                        highlights= '\x1b[0;37;41m' + str(NumberObj.numbers[j]) + '\x1b[0m' + '\x1b[0;30;44m' + str(NumberObj.numbers[j+1]) + '\x1b[0m'
                        posthighlights=str(NumberObj.numbers[j+2:])
                        output="Data:\n" + prehighlights + highlights + posthighlights



                


                #ADD I, J, SWAP, AND COMPARISON DATA TO OUTPUT
                output+="\n\ni:\t\t"+str(StateObj.i)
                output+="\nj:\t\t"+str(StateObj.j)
                output+="\nComparisons:\t"+str(StateObj.compares)
                output+="\nMovements:\t"+str(StateObj.swaps)
                output+="\nMemory Used:\t"+str(StateObj.memUsage)+" Bytes\n\n"

                for line in x.algo.lines:
                        if (x.algo.lines[StateObj.currentLine]==line):
                                output+= '\x1b[0;37;41m' + line + '\x1b[0m'
                        else:
                                output+=line
                
                #clear stdout
                os.system('clear')

                #print to cmdline
                print(output)


                #this is where the -w option comes into play
                if(wait):
                        raw_input("<hit enter to step>")

                #wait for a bit so that the output can actually be seen while playing
                time.sleep(StateObj.speed)



#random control flow to help parse cmdline args
if __name__ == "__main__":
        main(sys.argv[1:])


