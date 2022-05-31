#write  a  python program to find the median of three values.Go to the editor.
#1.expected output:
#2.input  first number:15
#3.input second number:26
#4.input third number:29
#5.the median is 26.0
num=float(input("enter number"))
num2=float(input("enter number"))
num3=float(input("enter number"))
if num2<num and  num<num3:
    print(num)
elif num3<num and num<num3:
    print(num)
elif num3<num2 and num3<num:
    print(num2)
elif num<num2 and num2<num3:
    print(num2)
elif num2<num3 and num3<num:
    print(num3)
elif num<num3 and num3<num2:
    print(num3)
else:
    print("none")