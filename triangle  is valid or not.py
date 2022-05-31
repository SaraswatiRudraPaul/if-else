#write a python program to input angle of a triangle and check wheather triangle is valid or not.
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
total=a+b+c
if total==180:
    print("it is a valid triangle")
else:
    print("it is not valid triangle")