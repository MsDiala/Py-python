'''
Python program to use Exception handling to catch divided by zero and divided by power of 2 exceptions

Input
enter the divident:
2
enter divisor:
8

Output
shouldnt be divided by zero or a power of 2


'''
#creating custom exception by inheriting the Exception class
class zeroor2(Exception):
    pass


def check(qt,wt):
    try:
        #checks if divisor = 0 or binary of(divisor - 1) contains only one
        #if wt =32 => wt-1 = 31 => bin(31) = 11111 => set('11111') = ['1'] => len(['1'])=1 so wt is power of 2
        #python gives 0b in front of binary so we replace 0b to get only the actual binary
        if(wt==0 or len(set(str(bin(wt-1)).replace('0b','')))==1):
            #condtion checking for divisor equal to 0 or power of 2
            #raising zero or power of 2 exception
            raise zeroor2
        else:
            print(qt/wt)
    except zeroor2:
        print('shouldnt be divided by zero or a power of 2')
msg = 'enter the divident:'
print(msg)
a = int(raw_input().strip())
msg = 'enter divisor:'
print(msg)
b = int(raw_input().strip())
check(a,b)
