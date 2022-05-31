#Take the age of 3 people by user and determine oldest and youngest among them.
num=int(input("enter the age"))
num2=int(input("enter the age"))
num3=int(input("enter the age"))
if num>num2 and num>num3 and num2<num3:
    print("num is oldest and num2 is youngest")
elif num>num2 and num>num3 and num3<num2:
    print("num is oldest and num3 is youngest")
elif num2>num and num2>num3 and num<num3:
    print("num2 is oldest and num is youngest")
elif num2>num and num2>num3 and  num3<num:
    print("num2 is oldest and num3 is youngest")
elif num3>num and num3>num2 and num2<num:
    print("num3 is oldest and num2 is youngest")
elif num3>num and num3>num2 and num<num2:
    print("num3 is oldest and num is youngest")
else:
    print("no oldest and no youngest")