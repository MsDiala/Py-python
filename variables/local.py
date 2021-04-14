'''
python program to use local variable by taking user input and print nearest power of 3

Input
4

Output
3
'''
#import math library for log functions
from math import log,floor,ceil
msg = 'enter the number:'
#printing message for user input
print(msg)
#taking input and casting it into integer
n = raw_input()
#stripping excess space in input
n = int(n.strip())
#log(x[,base]) gives the natural algorithm of log(x)/log(base)
#helpful in getting the nearest power to 3 as follows
#3^n = x+c where c is minimum for nearest power
#3^n = x+c => log(3^n) = log(x+c) => n*log(3) = log(x+c)
#let x+c = X
#=> n = log(X)/log(3) where n is the nearest nth power of 3
# similar in our case  3^n < x < 3^n+1 we calculate the minimum by
#n<log(x)/log(3)<n+1 and find the nearest power
minn = floor(log(n,3))
maxn = ceil(log(n,3))
if abs(n - 3**minn) <= abs(3**maxn - n):
    print(int(3**minn))
else:
    print(int(3**maxn))
