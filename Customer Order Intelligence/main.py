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
orders = 0
total_revenue = 0
units = 0

# Dynamic Dictionaries
customer_data = {}
product_data = {}
category_data = {}
province_data = {}

#Transaction log to check if an order_id is unique, duplicates result in an invlaid transaction
transaction_log = []

with open(filename,"r") as csvfile:
    for line in csv.DictReader(csvfile):
        # Initialse variables we want
        orders += 1 
        customer = line.get("customer")
        price = line.get("unit_price")
        product = line.get("product")
        category = line.get("category")
        quantity = line.get("quantity")
        transaction_id = line.get("order_id")
        province = line.get("province")


         # Validation rules 
         # Try block idea came from chatgpt but i found how to use it properly using W3Schools
        try :
            price = float(price)
            quantity = int(quantity)

            if price > 0 and quantity > 0 and transaction_id not in transaction_log and customer != "":
                revenue = price*quantity
                valid_transactions += 1
                transaction_log.append(transaction_id)
                units += quantity
                
            else : 
                invalid_transactions += 1

        except ValueError :
            invalid_transactions += 1
            continue


        # Dictionaries within dictionaries : data model 
        # Line 44-50 is from ChatGPT
        if customer not in customer_data:
            customer_data[customer] = { #We need to create a dictionary for the dictionary
                "Name":customer,
                "revenue": 0,
                "units": 0,
                "transactions": 0

            }
        # if customer_data[customer]["Name"] is None: #Stackoverflow
        #     customer_data[customer]["Name"] == "Unassgined Transactions"
        if product not in product_data:
            product_data[product] = {
                "Product":product,
                "revenue": 0,
                "units":0,
                "transactions":0
            }

        if category not in category_data:
            category_data[category]={
                "Category":category,
                "revenue":0,
                "units":0,
            }

        if province not in province_data:
            province_data[province]={
                "Province":province,
                "revenue":0,
                "units":0,
                "transactions":0
            }

        # We can now update specific keys within the nested dictionary because we have created them 
        customer_data[customer]["revenue"] += revenue
        customer_data[customer]["units"] += quantity
        customer_data[customer]["transactions"] += 1

        product_data[product]["revenue"] += revenue
        product_data[product]["units"] += quantity
        product_data[product]["transactions"] +=1

        category_data[category]["revenue"] += revenue
        category_data[category]["units"] += quantity

        province_data[province]["revenue"] += revenue
        province_data[province]["units"] += quantity
        province_data[province]["transactions"] +=1

for customer in customer_data:
    total_revenue += customer_data[customer]["revenue"]

print(f"Total Transactions : {orders}")
print(f"Valid Transactions : {valid_transactions}")
print(f"Invalid Transactions : {invalid_transactions}")
print(f"Total Revenue : R{total_revenue:.2f}") #rounding syntax from stackoverflow
print(f"Units Ordered : {units}")

average = total_revenue/units
print(f"Average Transaction Value: R{average:.2f}")
# Prints the internal dictionary for each customer 
print("------Customer Data--------")
for customer in customer_data: 
    print("Name: ",customer_data[customer]["Name"],"| Revenue: R",customer_data[customer]["revenue"],"| Units: ",customer_data[customer]["units"], "| Transactions: ",customer_data[customer]["transactions"])
    print("\n")
print("------Product Data--------")
for product in product_data:
    print("Product: ",product_data[product]["Product"],"| Revenue: R",product_data[product]["revenue"],"| Units: ",product_data[product]["units"], "| Transactions: ",product_data[product]["transactions"])
    print("\n")
print("-------Category Data--------")
for category in category_data:
    print("Category: ",category_data[category]["Category"],"| Revenue: R",category_data[category]["revenue"],"| Units: ",category_data[category]["units"])
    print("\n")

print("-------Province Data--------")
for province in province_data:
    print("Province: ",province_data[province]["Province"],"| Revenue: R",province_data[province]["revenue"],"| Units: ",province_data[province]["units"], "| Transactions: ",province_data[province]["transactions"])
    print("\n")

#print statements from GeeksForGeeks