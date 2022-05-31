#write a python program to find those numbers which are divisible by 7 and multiple of 5.between 1500 and 2700 (both include).
num=int(input("enter numbber"))
if num%7==0 and num%5==0:
    print("num is divisible by 7 and 5")
else:
    print("num is not divisible 7 and 5")