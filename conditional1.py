cost_price = float (input("Please Enter cost price "))
selling_price = float(input("Please enter selling price "))

if (cost_price<selling_price):
    amount = selling_price-cost_price
    print ("Total profit is " , amount )

else: 
    print("NO PROFIT !!!!")
