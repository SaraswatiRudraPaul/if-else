#write a program to accept two number and mathematical oprators and perform opration accordingly.
#like
#Enter first number:7
#Enter second number:9
#Enter oprator +
#Your answer:16
num=int(input("enter the first number"))
num2=int(input("enter second number"))
oprator=input("enter the oprator")
if oprator=="+":
    print(num+num2)
elif oprator=="-":
    print("num-num2")
elif oprator=="*":
    print("num*num2")
elif oprator=="%":
    print("num%num2") 
else:
    print("none")