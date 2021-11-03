import datetime
# naive time means dont know time zone

# import pytz # for using UTC time zone


# month is without 0  in front
d = datetime.date(2021,2,25)
print(d)

# every time I forget about the ()
tday = datetime.date.today()

print(tday.weekday())
# Monday is 0 Sunday is 6
print(tday.isoweekday())
# Monday is 1 Sunday is 7
print(tday.isoformat())
# output 2021-06-22 in this format

# tdelta = datetime.timedelta(days=7)
# print (tday - tdelta)
# or 
'''
3 mins
date 2 = date1 + timedelta

7.30 mins
datetime.time

t = datetime.time(9, 30, 45, 100000)
# hour, mins, sec, microsec



'''
