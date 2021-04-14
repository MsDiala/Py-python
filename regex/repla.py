'''
Python program to replace all the patterns like '[!*]' using loops

Input
enter the string:
[![![!*][!*]*]*]abc

Output
string before modification:[![![!*][!*]*]*]abc
abc

'''
import re
msg = 'enter the string:'
print(msg)
k = str(raw_input())
print('string before modification:'+k)
#replacing the pattern in string
#checking if there is any occurance of pattern
while(len(re.findall(r"\[!\*\]+",k))!=0):
    #replacing the pattern
    k = re.sub(r"\[!\*\]+",'',k)
print(k)
