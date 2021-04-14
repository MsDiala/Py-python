'''
python program to find the total occurences of a symbol in string using reqular expressions

Input
enter the main string:
1qaz!@#$!@#$zxswedc@#$%
enter the symbol you wish find occurences:
@

Output
@ occured 3 times in 1qaz!@#$!@#$zxswedc@#$%

'''
import re
msg= 'enter the main string:'
print(msg)
#getting main string from user
k = raw_input()
msg = 'enter the symbol you wish find occurences:'
print(msg)
l = len(k)
#getting symbol from user
s = raw_input()
#replacing input symbol in the string and find the decrease in lenth to find the occurences
#re's replaces all the matching patterns from given input and returns a replaced string
copy = re.sub(r''+s+'','',k)
print(s+' occured '+str(l-len(copy))+' times in '+k)
