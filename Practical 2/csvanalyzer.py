import csv 
#geeks for geeks documentation on reading csv files
filename = "Practical 2/Data/sales.csv" # already working in the python projects folder, now you must just access where the sales.csv file is
fields = [] #column names 
rows = [] #data rows 

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile) # we first open the CSV file in read mode 

    fields = next(csvreader) # read header a header is the first row of tect that names and defines the columns below it
    for row in csvreader:
        rows.append(row) 
    print("Total # of Rows: %d" %csvreader.line_num) #.line_num is the number of lines read from the source iterator
print("Field names:  " + ",".join(fields))
print("\n Data : \n")
for row in rows[:16]:
    for col in row:
        print("%10s" %col,end = " ")
    print("\n")