'''
program to find maxima minima for a quadratic equation for x^2 - 2x + 1 given as   1 -2 1

Input
enter the coefficients of quadratic equation:
1 4 4

Output
After differentiation the equation:2.0x+4.000000
the minima of given equation is at x=-2.000000

'''
msg = 'enter the coefficients of quadratic equation:'
print(msg)
equa = raw_input()
coef = list(map(float,equa.split()))
defe = []
#derivative loop
#power of x = length - 1 - i  for i = 0 => power = 2
for i in range(0,len(coef)):
    #checks if the power of x is 0
    if(len(coef)-i-1!=0):
        #appending the derivative equation ,power of x*quotient of x
        defe.append((len(coef)-i-1)*coef[i])
print('After differentiation the equation:'+str(defe[0])+'x%+f'%(defe[1]))
#getting solution : constant in derived equation/quotient of x
mai = float(-1*defe[1])/defe[0]
if(coef[0]>=0):
    print('the minima of given equation is at x=%f'%mai)
else:
    print('the maxima of given equation is at x=%f'%mai)
