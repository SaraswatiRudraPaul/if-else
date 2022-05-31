#write a programe to accept the cost price of a bike and disply the road and tax to be paid according to the following criteria.
#a.cost_price(in RS)           Tax
#b.>100000                      15%
#c.>50000 and <=100000          10%
#d.<=50000                      5%
cost_price=int(input("enter cost_price"))
if cost_price>100000:
    print("tax=",cost_price//100*5)
elif cost_price>50000 and cost_price<=100000:
    print("tax=",cost_price//100*10)
elif cost_price<=50000:
    print("tax=",cost_price//100*5)
else:
    print("no tex")