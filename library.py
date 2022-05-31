#Accept the  number of days from the user and calculate the charge for libary according to following.
#First five days:RS 2/day
#Six to ten days:RS 3/day
#Ten to 15 days:RS 4/day
#After 15 days:RS 5/day
day=int(input("enter number of day"))
if day>=0 and day<=5:
    print(day*2)
elif day>=6 and day<10:
    print(day*3)
elif day>10 and day<=15:
    print(day*4)
elif day>=15:
    print(day*5)
else:
    print("none")