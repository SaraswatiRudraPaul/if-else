#write a python program to check wheather a year is leap year or not.
year=int(input("enter year"))
if year%4==0:
    print("it is leap year")
elif  year%100==0 and year%400==0:
    print("it is centurion year")
else:
    print("it is not a leap year")