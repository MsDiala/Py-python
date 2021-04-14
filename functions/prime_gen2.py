'''
Python program to have a function to generate sequence of primes that are exactly at absoute difference of 1 with powers of two.

Input:
enter the number
1000

Output:
primes that are exactly at absolute difference of 1 with powers of 2 are:
3
5
7
17
31
127
257

'''
#checking whether the prime meets required condition
def soe(n,prime):
    p = 2
    while p*p<=n:
        if prime[p] ==True:
            i=p*2
            while i<=n:
                prime[i] = False
                i = i+p
        p+=1
    return prime
# checking whether the prime meets the required condition

def mp(n):
    #initializing an array
    prime = [True for i in range(0,n+1)]
    prime = soe(n,prime)
    k = 2
    while ((1<<k)-1<=n and (1<<k)+1<=n):
        #1<<k generates powers of 2
        num = (1<<k)-1
        if (prime[num]):
            print(num)
        num = (1<<k)+1
        if (prime[num]):
            print(num)
        k = k+1
msg = 'enter the number'
print(msg)
#reading the input from the console
#stripping extra spaces using strip and converting to integer
n = int(raw_input().strip())
print('primes that are exactly at absolute difference of 1 with powers of 2 are:')
#calling the function
mp(n)
