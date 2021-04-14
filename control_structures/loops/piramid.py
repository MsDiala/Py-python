'''
print the number pyramid of height n(input from user) using a single variable in entire program
  for 3
  1
  11
  111

Input
enter pyramid height:
5

Output
1
11
111
1111
11111

'''
msg = 'enter pyramid height:'
print(msg)
for i in range(0,int(input())):
    #as we use only one variable i.e i
    #power of 10 -1 = largest number in its digit space
    #e.g 1000-1=999 =>999/9=111
    print(str((10**(i+1)-1)/9))
