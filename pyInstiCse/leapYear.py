'''
Gregorian calendar introduced in 1582. 
@ The leap year is omitted three times every four hundred years. 
Hence 1700, 1800, 1900 are not, but 1600 and 2000 are.
The following rule is used to determine the kind of year:

if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
@otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year.
'''



"""

year = int(input("Enter a year: "))

if (year<1581):
    print(' Input must be after the start of Gregorian year 1582')
elif (year%4!=0):
    print('it is common year by 4')
elif (year%100!=0):
    print(' It is a leap year')
elif (year%400!=0):
    print('it is common year by 400')
else:
    print('it is a leap year loh')
    
"""


def is_year_leap(year):

    if (year<1581):
        print(' Input must be after the start of Gregorian year 1582')
        return False
    elif (year%4!=0):
        print('it is common year by 4')
        return False
    elif (year%100!=0):
        print(' It is a leap year')
        return True
    elif (year%400!=0):
        print('it is common year by 400')
        return False
    else:
        print('it is a leap year loh')
        return True
    


#
# put your code here
#

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("Test data and Result matches!")
	else:
		print("Failed")
