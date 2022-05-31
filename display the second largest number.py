#Acccept three numbers from the user and display the second largest number.
num=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number"))
if num>num2 and  num<num3:
    print("num is second largest number")
elif num2>num and num2<num3:
    print("num2 is second largest number")
elif num3>num and num3<num2:
    print("num3 is  second largest number")
else:
    print("no largest number")