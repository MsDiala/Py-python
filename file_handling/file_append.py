'''
Python program to append two files

Ouput
appended file data:
Hello programmer! you have successfully open text file
hello Ruby programmer
hello C programmer
hello C++ programmer
hello python programmer
hello buddy
'''
#using open and opening files using read rights(files to appended)
f1 = open('text.txt','r').read()
f2 = open('text1.txt','r').read()
#using open and opening files using write rights if file does not exist file gets created
#writing the data from f1 and f2 by concatinating them using string casting
f3 = open('text2.txt','w').write(str(f1)+str(f2))
#opeing appended data file
f  = open('text2.txt','r').read()
print('appended file data:')
print(f)
