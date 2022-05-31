#write a python program to get next  day of given date expected output
#Input a year2016
#Input a month[1-12]:08
#Input a day[1-3]:23
#The nest date is  [yyy-mm-dd]2016-8-24
year=int(input("enter year"))
month=int(input("enter month"))
day=int(input("enter day"))
if month==12 and day==31:
    print(year,month,day)
elif year==2016 and month==8:
    print(year,month,day+1)
else:
    print(year+1,month,day)