'''
Python program to check whether a given number is in a goemetric progression or not for a given initial value and factor

Input
enter initial term:
3
enter ratio in series(only integers):
5
enter number you want to check:
75

Output
yes its in series


'''
#getting user input
#get initial term in series
msg = 'enter initial term:'
print(msg)
#getting user input
a = raw_input()
#stripping extra spaces
a = int(a.strip())
msg = 'enter ratio in series(only integers):'
print(msg)
#get ratio in series only integers
r = raw_input()
#stripping extra spaces
r = int(r.strip())
msg = 'enter number you want to check:'
print( msg)
k = raw_input()
k = int(k.strip())
if(k%a==0 and k==a):
    print('you just entered the initial term again,yes its in series')
elif(k%a==0 and k%r==0 and k>a):
    #for G.P : a ar ar2 ar3 ......
    tmp = k/a #dividing by a(initial term)
    #now series consideration becomes
    # 1 r r2 r3 r4 .......
    while tmp!=1 and tmp >=r:#check for ratio exponential as in a.r^n
        tmp=tmp/r
    if(tmp==1):
        #storing console message
        msg = 'yes its in series'
        #print message
        print(msg)
    else:
        #storing console message
        msg = 'not in series'
        #print message
        print(msg)
else:
    #storing console message
    msg = 'not in series'
    #print message
    print(msg)
