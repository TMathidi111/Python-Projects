import csv 
#geeks for geeks documentation on reading csv files
filename = "Practical 2/Data/sales.csv" # already working in the python projects folder, now you must just access where the sales.csv file is
fields = [] #column names 
rows = [] #data rows 

# simialr to the student analyzer, we will go through the file row by row extracting data based on what column it is in according to the headers

total_revenue = 0
total_units_sold = 0
average_transaction_value = 0
electronics_count = 0
furniture_count = 0
stationery_count = 0
electronics_revenue = 0
furniture_revenue = 0
stationery_revenue = 0
laptop_revenue = 0
mouse_revenue = 0
office_chair_revenue = 0
keyboard_revenue = 0
desk_revenue = 0
monitor_revenue = 0
notebook_revenue = 0
pen_revenue = 0
highest_revenue_product = ""
highest_revenue = 0
highest_customer_revenue = 0
highest_spending_customer = ""

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile) # we first open the CSV file in read mode 

    fields = next(csvreader) # read header a header is the first row of tect that names and defines the columns below it
    for row in csvreader:
        rows.append(row) 
        price = float(row[5]) #logic is my own but i got help from stack overflow and the student analyzer 
        count = int(row[4])
        total_units_sold += count
        total_revenue += price*count
        product = row[2]
        customer = row[6]

        customer_revenue = price*count

        if row[3] == "Electronics":
            electronics_count += 1
            electronics_revenue += price*count #intellisense
        elif row[3] == "Furniture":
            furniture_count += 1
            furniture_revenue += price*count #intellisense
        elif row[3] == "Stationery":
            stationery_count +=1
            stationery_revenue += price*count #intellisense

        if product == "Laptop": 
            laptop_revenue += price*count
        elif product == "Office Chair":
            office_chair_revenue += price*count
        elif product == "Mouse":
            mouse_revenue += price*count
        elif product == "Keyboard":
            keyboard_revenue += price*count
        elif product == "Desk":
            desk_revenue += price*count
        elif product == "Monitor":
            monitor_revenue += price*count
        elif product == "Notebook":
            notebook_revenue += price*count
        elif product == "Pen":
            pen_revenue += price*count


        #intellisense added the if statements. Logic was my own
        if laptop_revenue > highest_revenue:
            highest_revenue = laptop_revenue
            highest_revenue_product = "Laptop"
        elif office_chair_revenue > highest_revenue:
            highest_revenue = office_chair_revenue
            highest_revenue_product = "Office Chair"
        elif mouse_revenue > highest_revenue:
            highest_revenue = mouse_revenue
            highest_revenue_product = "Mouse"
        elif keyboard_revenue > highest_revenue:
            highest_revenue = keyboard_revenue
            highest_revenue_product = "Keyboard"
        elif desk_revenue > highest_revenue:
            highest_revenue = desk_revenue
            highest_revenue_product = "Desk"
        elif monitor_revenue > highest_revenue:
            highest_revenue = monitor_revenue
            highest_revenue_product = "Monitor"
        elif notebook_revenue > highest_revenue:
            highest_revenue = notebook_revenue
            highest_revenue_product = "Notebook"
        elif pen_revenue > highest_revenue:
            highest_revenue = pen_revenue
            highest_revenue_product = "Pen"

        if customer_revenue > highest_customer_revenue:
            highest_customer_revenue = customer_revenue
            highest_spending_customer = customer
        
        

        

    average_transaction_value = total_revenue/total_units_sold 

    print("Total # of Rows: %d" %csvreader.line_num) #.line_num is the number of lines read from the source iterator
print("Field names:  " + ",".join(fields))
print("\n Data : \n")
for row in rows[:16]:
    for col in row:
        print("%10s" %col,end = " ")
    print("\n")
print(f"Total Revenue: {total_revenue}")
print(f"Total Units Sold: {total_units_sold}")
print(f"Average Transaction Value: {average_transaction_value:.2f}")
print(f"Products By Category: Electronics: {electronics_count} R{electronics_revenue:.2f}, Furniture : {furniture_count} R{furniture_revenue:.2f} , Stationery: {stationery_count} R{stationery_revenue:.2f}") 
print(f"Most Revenue Generating Product: {highest_revenue_product} R{highest_revenue:.2f}") #intellisense added the revenue code to the print statement. 
print(f"Highest Spending Customer: {highest_spending_customer} R{highest_customer_revenue:.2f}")
print(f"Highest Value Transaction: R{highest_customer_revenue:.2f}")
#intellisense added the revenue code to the print statement.

#All intenllisense did was write repetitve blocks of code for each product and category. The logic was my own. I also added the revenue code to the print statements.
# For checking for highest revenue i borrowed the logic used in the student analyzer to check for highest mark. I also used the same logic to check for highest spending customer.

#Notes : 
# Dictionaires would've helped store Key:Value pairs e.g. Laptop:12000
# Pay attention to what level you aggregate data, in this case it worked but you can make mistakes comparing values inside a loop when you are supposed to compare overall
# average transaction value = total revenue / number of transactions 
