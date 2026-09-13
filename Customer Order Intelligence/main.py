# Validity Rules 
# A valid transaction must have :
# A positive numeric price,quantity.
# A unique transaction id 
# A customer name 
# All fields must have a value
# We will need the following : 
# Total revenue per customer, units sold per customer , total revenue by product/category. With this we can do all else 
# Customer, Proudct and Category will need dynamic dictionaries also Province.

import csv

filename = "Customer Order Intelligence/Data/orders.csv"
valid_transactions = 0
invalid_transactions = 0
customer_data = {}

with open(filename,"r") as csvfile:
    for line in csv.DictReader(csvfile):
        # Initialse variables we want
        customer = line.get("customer")
        price = line.get("unit_price")
        product = line.get("product")
        category = line.get("category")
        quantity = line.get("quantity")

         # Validation rules 
        if price.isdecimal() and quantity.isnumeric():
            price = float(price)
            quantity = int(quantity)
            revenue = price*quantity
            valid_transactions += 1

        else :
            invalid_transactions += 1
            continue


        # Dictionaries within dictionaries : data model 
        # Line 31-43 is from ChatGPT
        if customer not in customer_data:
            customer_data[customer] = { #We need to create a dictionary for the dictionary
                "revenue": 0,
                "units": 0,
                "transactions": 0

            }
        # We can now update specific keys within the nested dictionary because we have created them 
        customer_data[customer]["revenue"] += revenue
        customer_data[customer]["units"] += quantity
        customer_data[customer]["transactions"] += 1

print(valid_transactions)
print(invalid_transactions)

        
        
