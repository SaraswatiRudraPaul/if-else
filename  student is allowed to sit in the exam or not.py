#A student will not be allowed to sit in an exam if his/her attendence is less then 75%.Take following input from the user.number of classes attended and print percentage of class attended is the student is allowed to sit in the exam or not.
attended=int(input("enter the class attended"))
held=int(input("enter the class held"))
percentage=attended*held/100
if percentage>=75:
    print("allow to sit in the exam")
else:
    print("not allow to sit in the exam")