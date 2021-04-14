'''
Python program to find whether the number is odd and multiples of nine

Input
Enter the number
27

Output
27 is both odd number and a multiple of 9

'''
#take input from user
msg = 'Enter the number'
print(msg)
a = raw_input()
#stripping spaces
a = a.strip()
#Converting to integer
a = int(a)
if(a%2!=0 and a%9==0):#by not 2 and by 9 true
    print('%d is both odd number and a multiple of 9'%a)
elif(a%2!=0 and a%9!=0):#by not 2 and by not 9
    print('%d is odd number but not a multiple of 9'%a)
elif(a%2==0 and a%9==0):#by 2 and by 9 true
    print('%d is not odd number but a multiple of 9'%a)
else:
    print('%d is not odd number and not a multiple of 9'%a)
