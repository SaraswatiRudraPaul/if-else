#write a python program to check wheather the triangle is equilateral,isosceles,or scalene triangle.
a=int(input("enter a angle"))
b=int(input("enter a angle"))
c=int(input("enter a angle"))
if (a==b==c):
    print("equilateral triangle")
elif a==b or b==c or c==a:
    print("isosceles triangle")
else:
    print("scalene triangle")