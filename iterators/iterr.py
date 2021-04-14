'''
Python program to use iterators to generate the multiples of two and three

Input
10

Output
multiples of both 2 and 3 are:
[6, 12, 18, 24, 30, 36, 42, 48, 54, 60]

'''
#importing iteration tools
import itertools
msg = 'enter the number of terms:'
n = int(raw_input().strip())
#using combinations and generating the multiples of 2 and 3(both) i.e multiples of 6
k = itertools.combinations([6*i for i in range(1,n+1)],1)
ll = [k.next()[0] for i in range(0,n)]
print('multiples of both 2 and 3 are:')
print(ll)
