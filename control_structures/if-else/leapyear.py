'''
Python program to check if the input year is a leap year or not by using following conditions
  The year can be evenly divided by 4, unless;
  The year can be evenly divided by 100, it is NOT a leap year, unless;
  The year is also evenly divisible by 400. Then it is a leap year.

Input
Enter year:
1992

Output
1992 is a leap year

'''
msg = 'Enter year:'
print(msg)
year = raw_input()
#stripping spaces and converting to int
year = year.strip()
#integer conversion
year = int(year)
#first divisible by 4 and not by 100 or second divisible by 400
if (year % 4 == 0 and year % 100!=0) or year%400==0:
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
