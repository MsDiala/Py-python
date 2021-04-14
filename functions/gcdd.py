'''
Write a python program to have a function to find gcd of two numbers

Input
enter two numbers whose GCD is to be found
24
8

Output
The GCD is :8


'''
def gcdd(a,b):
    #stopping condition for recursion that is bigger number is divisible by smaller number in gcd parameters
    #max(1,2) returns 2 and min(1,2) returns 1
    #if we pass two numbers as parameters it first checks the division condition of maximum and minimum
    #returns minimum if condition is successful
    if(max(a,b)%min(a,b)==0):
        return min(a,b)
    else:
        #returns gcd of remainder and divisor
        return gcdd(min(a,b),max(a,b)%min(a,b))
#reading the input from user
#first number
msg = 'enter two numbers whose GCD is to be found'
#printing message to the console
print(msg)
a = int(raw_input().strip())
#second number
b = int(raw_input().strip())
print('The GCD is :%d'%gcdd(a,b))
