#write a program to calculate the electricity bill (accept number of unit from user)according to the following criteria.
#     unit              price
# first 100 units       no charge
#next 100 units         RS5 per unit
#after200 units         RS100 per units
#For example if input unit is 350 than total bill amount is RS-2000
unit=int(input("enter unit"))
if unit<=100:
    print("no charge")
elif unit>100 and unit<=200:
    a=unit-100
    print("bill=",a*5)
elif unit>200:
    a=unit-100
    b=100*5
    c=a-100
    d=c*10
    e=b+d
    print("bill=",e)
else:
    print("no bill")