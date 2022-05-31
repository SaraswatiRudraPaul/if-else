#A shop will give a discount of 10% if the cost of the purced quantity is more than 1000.Ask the user for quantity supose one unit will cost 100.Jude and print total cost for user.
quantity=int(input("enter quantity"))
total_cost=quantity*100
if total_cost>1000:
    Discount=quantity*10/100
    total_cost=quantity-Discount
    print(total_cost)
else:
    print("no discount")