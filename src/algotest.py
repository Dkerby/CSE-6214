from __future__ import print_function

import os,sys, getopt 
#os used for clearing the cmdline output, 
#sys and geopt used for cmdline arguments

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
        if(algochoice<1 or algochoice>5):
                print("That is not one of the available algorithms")
                sys.exit(2)

        if(speed<0.0001 or speed>5.0):
                print("That is either too fast or too slow")
                sys.exit(2)

        print('Generating array of size', arrsize)
        print('Algorithm choice is ', algochoice)


        #creates NumberList, State, and Algorithm objects
        x=alg.Algorithm(True, algochoice, speed, arrsize) #pass State object into Algorithm along with the choice of algorithm
        state=x.getState()
        #while algorithm is not complete, keep on steppin'

        while(state.sorting):

                #step it up!
                x.step()
                state=x.getState()
                output=x.getFormat()

                #ADD I, J, SWAP, AND COMPARISON DATA TO OUTPUT
                output+="\n\ni:\t\t"+str(state.i)
                output+="\nj:\t\t"+str(state.j)
                output+="\nComparisons:\t"+str(state.compares)
                output+="\nMovements:\t"+str(state.swaps)
                output+="\nMemory Used:\t"+str(state.memUsage)+" Bytes\n\n"


		#Higlighting the pseudocode
                for line in x.algo.lines:
                        if (x.algo.lines[state.currentLine]==line):
                                output+= '\x1b[0;37;41m' + line + '\x1b[0m'
                        else:
                                output+=line
                
                #clear stdout
                os.system('clear')

                #print to cmdline
                print(output)


                #this is where the -w option comes into play
                if(wait):
                        input("<hit enter to step>")



#random control flow to help parse cmdline args
if __name__ == "__main__":
        main(sys.argv[1:])


