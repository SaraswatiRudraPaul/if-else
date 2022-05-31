#write a python program to input electricity unit charge and calculate total electricity bill according to the given condiotion.
#for first 50 units RS.0.50/unit
#for next 100 units RS.0.75/unit
#for next 100 units RS.1.20/unit
#for next above 250 RS.1.50/unit
#An additional surcharge of 20% is added to the bill
unit_charge=int(input("enter unit_charge"))
if unit_charge>=1 and unit_charge<50:
    total_bill=unit_charge*0.50+20/100
    print(total_bill)
elif unit_charge>=51 and unit_charge<=100:
    total_bill=unit_charge*0.75+20/100
    print(total_bill)
elif unit_charge>=100 and unit_charge<=150:
    total_bill=unit_charge*1.20+20/100
    print(total_bill)
elif unit_charge>=150 and unit_charge<=250:
    total_bill=unit_charge*1.50+20/100
    print(total_bill)
else:
    print("no total bill")