'''
Python program to find derivative and integral of polynomial,for polynomial x3 + 4x2 + 2x - 1 given in form of 1 4 2 -1

Input
enter the coefficients:
5 4 3 2 1

Output
after differentiation,the equation is:+20.000000x^3 +12.000000x^2 +6.000000x^1 +2.000000
after integration the equation is:+1.000000x^5 +1.000000x^4 +1.000000x^3 +1.000000x^2 +1.000000x^1 +C

'''
msg = 'enter the coefficients:'
print(msg)
# enter equation that is in form of  x3+4x2+2x-1 as 1 4 2 -1
equa = raw_input()
#spliting string into int list using map and split

coef = list(map(float,equa.split()))
defe = []
#integration loop for getting integration of equation
for i in range(0,len(coef)):
    if(len(coef)-i-1!=0):
        defe.append((len(coef)-i-1)*coef[i])
str1 = 'after differentiation,the equation is:'
#using loops and generating user understandable equation
for i in range(0,len(defe)):
    #if power of x not equal to zero condition
    if(len(defe)-i-1 != 0):
        #for i = o
        #str1=str1+'coefficient of x^n i.e defe[0]'+X+'power of x(n(length - 0 - 1))'
        str1=str1+''.join(str('%+f'%defe[i])+'x^'+str(len(defe)-i-1))
    else:
        str1=str1+''.join(str('%+f'%defe[i]))
    #condition for last term with power = 0
    if i != (len(defe)-1):
        str1=str1+' '
print(str1)
str2 = 'after integration the equation is:'
dd = [len(coef)-i for i in range(0,len(coef))]
for i in range(0,len(coef)):
    #for i = o
    #str2=str2+'coefficient of x^n i.e defe[0]'+X+'power of x(n(length - 0))'
    str2=str2+''.join(str('%+f'%(float(coef[i])/dd[i]))+'x^'+str(len(coef)-i))
    str2=str2+' '
#adding constant
str2 = str2+'+C'
print(str2)
