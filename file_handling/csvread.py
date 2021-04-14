'''
Python program to open a csv file and print only the second column in the file

Output
the data in second column is :
2
two
dho
rendu

'''
#import csv module
import csv
import sys
#using DictReader in csv for getting data column wise that is first row is used for referring the rows below
#open csv file cc.csv and see it for yourself for better understanding
#if you want to know more modules in csv, simply go for python docs online
print('the data in second column is :')
for d in csv.DictReader(open('cc.csv')):
    print(str(d['second']))
