#Accept the age,sex,("M","F")number of days and display the wages accordingly
#if age does not fall in any range then display the following message:"Enter appropriate age"
#Age          Sex        Wage/day
#=18 and <30   M         700
#              F         750
#>=30 and <=40 M         800
#              F         850
age=int(input("enter age"))
sex=input("enter sex")
day=int(input("enter day"))
if age>=18 and age<30 and sex=="M":
    Wage=day*700
    print("wage",Wage)
elif age>=18 and age<=30 and sex=="F":
    Wage=day*750
    print("Wage",Wage)
elif age>=30 and age<=40 and sex=="M":
    Wage=day*800
    print("Wage",Wage)
elif age>=30 and age<=40 and sex=="F":
    Wage=day*850
    print("wage",Wage)
else:
    print("none")