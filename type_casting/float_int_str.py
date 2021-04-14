'''
Python program to take a float input from user and convert it into integer and string in respective manner

Input
3.6

Output
The int value is:3
Converting into string:3.6
The int value is 3
Converting into string: 3.6
'''
#taking input from user
#message variable
msg = 'enter a float value:'
#printing message for user input
print(msg)
a = raw_input()
#stripping extra spaces in input
a = float(a.strip())
#explicit casting
#converting into integer
k = int(i)
print('The int value is:%d'%k)
#converting into string
k = str(i)
print('Converting into string:'+k)
#you can also do it by implicit casting
#converting float number to integer
print('The int value is %d'%i)
#converting float number to string
print('Convering into string: %s'%i)
