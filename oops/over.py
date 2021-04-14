'''
Python program to Use Function Overridingin a class.

Output
B's hello
A's GoodBye

'''
class A():
    #constructor of A
    def __init__(self):
        self.__x = 1


    #m1 function of parent
    def m1(self,Ab):
        print('A\'s '+str(Ab))


class B(A):
    #constructor of B
    def __init__(self):
        self.__y = 1

    #m1 function of child
    #    print("m1 from B")
    def m1(self,Ab):
        print('B\'s '+str(Ab))

b = A()
c = B()
#c.m1() prints hello from B
c.m1('hello')
b.m1('GoodBye')
