'''
Python program to have a function to find whether a given number is armstrong number or not

Input
enter a number
1634

Output
1634 is a armstrong number
'''
#armstrong number function
#An n-digit number that is the sum of the nth powers of its digits is called an n-narcissistic number. It is also sometimes known as an Armstrong number,
def arms(n):
    #converting n into string so we can access each digit individually using the string indexing
    ns = str(n)
    #summ variable for comparsion
    summ = 0
    for i in range(0,len(ns)):
        #summing the lenth power of each digit into summ variable
        summ = summ+int(ns[i])**len(ns)
    if(summ == n):#comparing the summ and n to check the equality
        return True
    else:
        return False
msg = 'enter a number'
print(msg)
k = int(input())
if(arms(k)):
    print('%d is a armstrong number'%k)
else:
    print('%d is not a armstrong number'%k)
