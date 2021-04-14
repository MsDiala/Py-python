'''
Python program to take input a sequence of numbers from user and store it in a list or array

Input
3
11
12
13

Output
[11, 12, 13]
'''
msg = 'enter the number of elements:'
#printing message for user input
print(msg)
# taking length of list to be inputted
a = raw_input()
#stripping extra spaces in input
a = int(a.strip())
#empty list
num = []
print('Enter the elements:')
for i in range(0,a):
    #using append function of lists and appending the data into empty list
    num.append(int(input()))
print('Elements of list are:')
print(num)
