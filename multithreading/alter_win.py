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

#importing threads from threading
from threading import Thread
import time
def runA(k):
        i = 1
        while(i<=k):
                #print multiple of 2
                print(str(int(2*i))+'\n')
                time.sleep(1)
                i+=1

def runB(k):
        j = 1
        while(j<=k):
            #print multiple of 3
                print(str(int(3*j))+'\n')
                time.sleep(1)
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
