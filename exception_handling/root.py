'''
Python program to 2.use exception handling to prevent the calculation of roots of quadratic equation if root as complex

Input
enter the equation in the form of 1 2 1 if equation is x^2 + 2x + 1:
1 1 1

Output
roots are imaginery so calculation stopped


'''
#defining the class for our exception
#our custom exception inherits the Exception class for raising the exception of complex roots
class complexerror(Exception):
    pass
#taking the input and splitting it and converting it into integer list using map and split function in python
msg = 'enter the equation in the form of 1 2 1 if equation is x^2 + 2x + 1:'
print(msg)
k = raw_input()
k = k.strip()
k = list(map(int,k.split()))
try:
    t = k[1]**2-4*k[0]*k[2]
    if(t<0):
        #raising exception as determinant<0
        raise complexerror
    else:
        print('roots are :')
        print((-1*k[1]+float(t)**0.5)/(2*k[0]))
        print((-1*k[1]-float(t)**0.5)/(2*k[0]))
except complexerror:#exception body
    print('roots are imaginery so calculation stopped')
