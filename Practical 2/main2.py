import csv 

filename = "Practical 2/Data/sales.csv"

#attemping to use dictionaires to read the csv file 
# documentation retrieved from geeks for geeks
with open(filename,"r") as csvfile:
    for line in csv.DictReader(csvfile):
        print(line)

#TO DO:
# Calculate revenue
# Calculate average transaction value 
