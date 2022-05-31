#write a program to check wheather a number entered is a three digit number or not.
a=int(input("enter a number"))
if a>=100 and a<=999:
    print("Three digit number")
else:
    print("not a three digit number")