#write a python program to input basic salary of an enploye and calculate its gross salary according to following.
#Basic salary<=10000:HRA=20%DA=80%
#Basic salary<=20000:HRA=25%DA=90%
#Basic salary>=20000:HRA=30%DA=95%
basic_salary=int(input("enter salary"))
if basic_salary<=10000:
    HRA=(basic_salary*20/100)
    DA=(basic_salary*80/100)
    Gross_salary=(basic_salary+HRA+DA)
    print(Gross_salary)
elif basic_salary<=20000:
    HRA=(basic_salary*25/100)
    DA=(basic_salary*90/100)
    Gross_salary=(basic_salary+HRA+DA)
    print(Gross_salary)
elif basic_salary>20000:
    HRA=(basic_salary*30/100)
    DA=(basic_salary*95/100)
    Gross_salary=(basic_salary+HRA+DA)
    print(Gross_salary)