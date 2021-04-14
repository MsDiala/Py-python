'''
in physics, contact between objects during a collision leads to loss of force as no medium is perfect.
likely we are having n medium in a plane each of equal length followed by qouitient of reduction, In can be well
explained using the following example
person throws a ball on plane from certain height h of n medium your job is to find distance traveled in plane
and the medium is repetted in cyclic order and height is only considered in integers
input:
  3(number of medium)
  4(length of each)
  5(height from which ball is thrown)
  2(distance travelled for each step)
  0.1
  0.3
  0.5
  output:
  first  step 5*0.9= 4 dist = 2
  second step 4*0.9= 3 dist = 4
  third  step 3*0.7= 2 dist = 6
  fouth  step 2*0.7= 1 dist = 8
  fifth  step 1*0.5= 0 dist = 10
so,the result is 10(ten) steps

Input
enter total number of mediums:
3
enter length of medium:
3
enter height from which ball is thrown:
10
enter distance travelled in each step:
4
now enter qoutients of loss for 3 mediums:
1 medium :0.2
2 medium :0.3
3 medium :0.4

Output
distance traveled by ball is 24
'''
msg = 'enter total number of mediums: '
print(msg)
k = int(raw_input().strip())
msg = 'enter length of medium: '
print(msg)
l = int(raw_input().strip())
msg = 'enter height from which ball is thrown: '
print(msg)
h = int(raw_input().strip())
msg = 'enter distance travelled in each step:'
print(msg)
d = int(raw_input().strip())
print('now enter qoutients of loss for %d mediums:'%k)
kq =[]
for i in range(0,k):
    #appending into list, the converted float from input
    kq.append(float(input('%d medium :'%(i+1))))#input can print messages given as parameters
h1 = h
d1 = 0
while h1!=0:
    fl = k*l
    for i in range(0,k): #for medium check
        if (h1!=0): #height not equal to zero
            tt = d1%fl #medium repeatition check
            d1=d1+d #distance increament per step
            h1 = int(h1*(1-kq[int(tt/l)]))
print('distance traveled by ball is %d'%d1)
