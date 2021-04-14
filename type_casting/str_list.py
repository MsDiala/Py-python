'''
Python progrma to take a string and convert it into list or array by using the spaces in the string as delimiter

Input
python ruby php

Output
Entered string :python ruby php
List generated is:
['python', 'ruby', 'php']
'''
msg = 'Enter the string'
print(msg)
k = raw_input()
print('Entered string :'+k)
#using split and type casting we convert string to list
li = list(k.split(' '))
print('List generated is:')
print(li)
