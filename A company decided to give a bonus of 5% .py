#A company decide to give a bonus of 5% to an employe if his/her year of service is more than 5 years.Ask users for their salary and year of service and print the net bonus amount.
salary=int(input("enter salary"))
year_of_service=int(input("enter service year"))
if (year_of_service>5):
    print("bonus",5/100*salary)
else:
    print("no bonus")