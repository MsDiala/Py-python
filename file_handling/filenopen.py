'''
Python program to open a text file and print the nth line in text file if nth line does not exist print 'no data'

Input
enter the line number:
4

Ouput
4th line:hello python programmer

'''
#opeing the text file
f = open('text1.txt','r')
#getting nth line number from user
msg = 'enter the line number:'
print msg
n = int(raw_input().strip())
#split the file based on lines using \n escape code as \n indcates new line
dd = list(f.read().split('\n'))
if(len(dd)>=n+1):#checking if nth line exists in file or not
    print('%dth line:'%n+str(dd[n-1]))
else:
    print('no data')
