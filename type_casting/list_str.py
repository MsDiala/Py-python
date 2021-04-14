'''
Python progrma to convert a list or array into a string

Output
123456
'''
# its ok if you are unable to do it as it uses list comprehensions
k =[1,2,3,4,5,6]
print('list taken:')
print(k)
# using join and list comprehensions to join all elements into a string
string = ''.join(str(i) for i in k)
print('converted string:'+string)
