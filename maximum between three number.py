#write a python program to find maximum between three number.
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if a>b and a>c:
    print("a is maximum")
elif b>a and b>c:
    print("b is maximum")
elif c>a and c>b:
    print("c is maximum")
else:
    print("no maximum")