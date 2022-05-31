#write a  python program to calculate profit or loss.
actual_cost=int(input("enter a  amount"))
selling_cost=int(input("enter a amount"))
if (actual_cost<selling_cost):
    print("profit")
elif (actual_cost>selling_cost):
    print("loss")
else:
    print(" no profit no loss")