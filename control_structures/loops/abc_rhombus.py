'''
using loops of your choice and print as follows for a given input
input:
3
9
output:
----a----
---bbb---
--ccccc--
---bbb---
----a----

Input
enter number:
6
enter width:
11

Output
-----a-----
----bbb----
---ccccc---
--ddddddd--
-eeeeeeeee-
fffffffffff
-eeeeeeeee-
--ddddddd--
---ccccc---
----bbb----
-----a-----

'''
msg = 'enter number:'
print(msg)
#getting the half height of pyramid
a = raw_input()
#stripping spaces
a = int(a.strip())
msg = 'enter width:'
print(msg)
#getting width from user
n = raw_input()
#stripping spaces in input
n = int(n.strip())
for i in range(0,a):
    #using center function for padding from string functions
    #using ascii codes for printing the getting the alphabet based on loop va
    #increament loop
    print(str(chr(97+i)*(2*i+1)).center(n,'-'))
for i in range(1,a):
    #decreament loop
    print(str(chr(97+a-i-1)*(2*(a-i)-1)).center(n,'-'))
