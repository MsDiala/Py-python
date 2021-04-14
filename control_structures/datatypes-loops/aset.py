'''
Python program to use array as set in the program to store only unique items in a array or list

Input
enter list of your choice with repetitions:
1 2 4 1 4 5 6 3

Output
['1', '3', '2', '5', '4', '6']


'''
#message variable
msg = 'enter list of your choice with repetitions:'
#printing message for user input
print(msg)
#taking data from user in console
a = raw_input()
#stripping the excess zeroes in input using strip() function
a = a.strip()
#splitting the raw input into individual elements and storing in list
b = list(a.split())
#set is a datatype in python only stores unique items in list
#conversion list->set->list
c = list(set(b))
#printing the unique item list
print(c)
