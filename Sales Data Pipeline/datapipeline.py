import csv 

filename = "Sales Data Pipeline/Data/sales_raw.csv"
revenue = 0
invalid_transactions = 0
valid_transactions = 0
units_sold = 0
average_transaction_value = 0

# thabo_total = 0
# naledi_total = 0
# lerato_total = 0
# mpho_total = 0

# thabo_transactions= 0
# naledi_transactions = 0
# lerato_transactions = 0
# mpho_transactions = 0

# thabo_units = 0
# naledi_units = 0
# lerato_units = 0
# mpho_units = 0

# ChatGPT : The problem is that we are creating variables based on the data 
# Instead we want the data to create the dictionary entries 

customer_revenue = {} #Empty Dictionary for customers
product_revenue = {} # Empty Dictionary for Products
category_revenue = {} # Empty Dictionary for categories

# laptop_total = 0
# mouse_total = 0
# office_chair_total = 0
# keyboard_total = 0
# monitor_total = 0
# notebook_total = 0
# pen_total = 0

# electronics_revenue = 0
# furniture_revenue = 0
# stationery_revenue = 0

with open(filename,"r") as csvfile:
    for line in csv.DictReader(csvfile): #creating a dictionary
        price = line.get("unit_price") # documentation from realpython.
        quantity = line.get("quantity")
        customer = line.get("customer")
        product = line.get("product")
        category = line.get("category")

        if price.isnumeric() and quantity.isnumeric(): #checking if the values are numeric
            price = float(price)
            quantity = int(quantity)
            valid_transactions += 1
            transaction_revenue = price * quantity
        else: 
            invalid_transactions += 1
            continue #skip the rest of the loop and go to the next iteration

        revenue += price * quantity#float for price to allow decimals, int for quantity to have whole numbers only
        units_sold += quantity

        # if customer == "Thabo":
        #     thabo_total += price * quantity
        #     thabo_transactions += 1
        #     thabo_units += quantity
        # elif customer == "Naledi":
        #     naledi_total += price * quantity 
        #     naledi_transactions += 1
        #     naledi_units += quantity
        # elif customer == "Lerato":
        #     lerato_total += price * quantity
        #     lerato_transactions += 1
        #     lerato_units += quantity
        # elif customer == "Mpho":
        #     mpho_total += price * quantity
        #     mpho_transactions += 1
        #     mpho_units += quantity

        if customer not in customer_revenue: #If this customer does not currently exist as a key in the dictionary 
            customer_revenue[customer] = 0 
        customer_revenue[customer] += transaction_revenue


         # 'is not' tests dictionary membership
         # We create a place to store a customers revenue starting from 0
         # We add to our running total. Python adds the value to the respective customer.
         # First set at 0 because we are initialising

        # if product == "Laptop":
        #     laptop_total += price*quantity
        # elif product == "Mouse":
        #     mouse_total += price*quantity
        # elif product == "Office Chair":
        #     office_chair_total += price*quantity
        # elif product == "Keyboard":
        #     keyboard_total += price*quantity
        # elif product == "Monitor":
        #     monitor_total += price*quantity 
        # elif product == "Notebook":
        #     notebook_total += price*quantity
        # elif product == "Pen":
        #     pen_total += price*quantity

        if product not in product_revenue:
            product_revenue[product] = 0
        product_revenue[product] += transaction_revenue

        # if category == "Electronics":
        #     electronics_revenue += price*quantity
        # elif category == "Furniture":
        #     furniture_revenue += price*quantity
        # elif category == "Stationery":
        #     stationery_revenue += price*quantity

        if category not in category_revenue:
            category_revenue[category] = 0
        category_revenue[category] += transaction_revenue

average_transaction_value = revenue/valid_transactions
# customer_revenue = [thabo_total, naledi_total, lerato_total, mpho_total]
highest_revenue = max(customer_revenue)

print(f"Revenue: R{revenue}")
print(f"Invalid Transactions: {invalid_transactions}")
print(f"Valid Transactions: {valid_transactions}")
print(f"Units Sold: {units_sold}")
print(f"Average Transaction Value: R{average_transaction_value:.2f}")
# print("Revenue by Customer:")
# print(f"Thabo: R{thabo_total} Transactions: {thabo_transactions} Units Sold: {thabo_units}")
# print(f"Naledi: R{naledi_total} Transactions: {naledi_transactions} Units Sold: {naledi_units}")
# print(f"Lerato: R{lerato_total} Transactions: {lerato_transactions} Units Sold: {lerato_units}")
# print(f"Mpho: R{mpho_total} Transactions: {mpho_transactions} Units Sold: {mpho_units}")
# print(f"Highest Revenue: R{highest_revenue} - Thabo")
# print("Revenue by Product:")
# print(f"Laptop: R{laptop_total}")
# print(f"Mouse: R{mouse_total}")
# print(f"Office Chair: R{office_chair_total}")
# print(f"Keyboard: R{keyboard_total}")
# print(f"Monitor: R{monitor_total}")
# print(f"Notebook: R{notebook_total}")
# print(f"Pen: R{pen_total}")
# print("Revenue by Category:")
# print(f"Electronics: R{electronics_revenue}")
# print(f"Furniture: R{furniture_revenue}")
# print(f"Stationery: R{stationery_revenue}")
print(highest_revenue)
for customer,revenue in customer_revenue.items():
    print(f"{customer}: R{revenue}")

print(customer_revenue)