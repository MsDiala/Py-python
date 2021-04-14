'''
Python program that should find the percentage of a student for input given in following manner
3
rag 78 56 72
teja 83 67 78
bhavana 83 75 67
bhavana
output: 75

Input
Enter the number of students
5
Enter the details of students:
rag 89 90 91
tej 86 94 90
bhavana 88 92 90
srinu 89 91 90
ravi 89 90 93
enter name of student
rag

Output
percentage is 90.00


'''
#take in user input with multiple types in string format
msg = 'Enter the number of students'
print(msg)
#taking input from user stripping extra spaces and converting into integer
n = int(raw_input().strip())
marks = []
print('Enter the details of students:')
for _ in range(n):
    #making list of raw data
    marks.append(list(raw_input().split(' ')))
#get name for percentage finding
msg = 'enter name of student'
print(msg)
c = str(raw_input())
for x in marks:
    if (x[0] == c):
        #summing the marks
        total = int(x[1])+int(x[2])+int(x[3])
        #finding average for getting marks
        total = total/3
        print('percentage is %.2f'%total)
