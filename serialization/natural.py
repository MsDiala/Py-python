'''
Python program to Use serialization for getting a series of natural numbers

Input
enter the nth term:
20

Output
serialized numbers
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

'''
#importing pickle module
import pickle
msg = 'enter the nth term:'
print(msg)
#storing in pickle dumps
#                                       list comprehension for getting natural number range after stripping spaces from input
x = pickle.dumps(range(1,int(raw_input().strip())+1))
print('serialized numbers')
#printing the serialized data using pickle loads
print(pickle.loads(x))
