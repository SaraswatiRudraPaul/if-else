#A school has following rules for garding system.
#a.Below25-F
#b.25to45-E
#c.45to50-D
#d.50-60-C
#e.60-80-B
#f.above-80-A
#Ask user to enter marks and print the corresponding grad.
score=int(input("enter score"))
if score<25:
    print("gradeF")
elif score>25 and score<45:
    print("grade E")
elif score>45 and score<50:
    print("grade D")
elif score>50 and score<60:
    print("gradeC")
elif score>60 and score<80:
    print("grade B")
elif score>80:
    print("grade A")
else:
    print("no grade")