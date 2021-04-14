'''
Python program to use multithreading to print alternatly multiples of three and two

Input
enter the nth term:3
3
2


6
4


6
9

'''
import sys
#colors is not python library its defined in colors.py file don't forget to include the file in same directory of execution
from colors import *
#importing threads from threading
from threading import Thread
import time
def runA(k):
        i = 1
        while(i<=k):
            #print multiple of 2
            sys.stdout.write(RED)
            print('%d\n'%(2*i))
            time.sleep(1.500)
            i+=1



def runB(k):
        j = 1
        while(j<=k):
            #print multiple of 3
            sys.stdout.write(CYAN)
            print('%d\n'%(3*j))
            time.sleep(1.500)
            j+=1


if __name__ == "__main__":
        k = int(input('enter the nth term:'))
        #setting target for threads
        t1 = Thread(target = runA,args=(k,))
        t2 = Thread(target = runB,args=(k,))
        #starting threads
        t1.start()
        t2.start()
        #while for running of threads
        #while i<=k and j<=k:
        #        pass
