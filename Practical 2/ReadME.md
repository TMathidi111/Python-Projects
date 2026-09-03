# Practical 02 — Sales Data Analyzer

## Overview

Practical 02 is a Python-based Sales Data Analyzer that reads sales transaction data from a CSV file and calculates a range of business-related statistics.

The purpose of this practical was to move beyond basic Python fundamentals and begin working with **realistic structured data**, while developing problem-solving skills around reading files, extracting data, performing calculations, and aggregating information.

The practical was completed using **standard Python libraries**, without using Pandas or other data-analysis frameworks.

## Learning Objectives

The main objectives of this practical were to:

* Read and process CSV data using Python.
* Understand how rows and columns are represented in a CSV file.
* Convert strings from a CSV file into appropriate numerical data types.
* Calculate derived values such as transaction revenue.
* Aggregate numerical information across multiple records.
* Identify maximum values from a dataset.
* Group information by categories and products.
* Begin understanding dictionaries as a way of organising data.
* Recognise the limitations of repetitive and hard-coded code.
* Practise solving a data-processing problem independently.

## Dataset

The input dataset is:

`Data/sales.csv`

Each transaction contains the following fields:

| Field            | Description                           |
| ---------------- | ------------------------------------- |
| `transaction_id` | Unique identifier for the transaction |
| `date`           | Date of the transaction               |
| `product`        | Product purchased                     |
| `category`       | Product category                      |
| `quantity`       | Number of units purchased             |
| `unit_price`     | Price of one unit                     |
| `customer`       | Customer who made the purchase        |

Transaction revenue is calculated using:

`quantity × unit_price`

## Analysis Performed

The program processes the sales data and calculates:

* Total revenue
* Total units sold
* Number of transactions
* Average transaction value
* Revenue by product
* Revenue by category
* Highest-revenue product
* Highest-spending customer
* Highest-value transaction

The program also produces a readable summary of the analysis in the terminal.

## Python Concepts Used

This practical introduced and reinforced the following concepts:

* `import`
* File handling with `open()`
* `csv.reader`
* `csv.DictReader`
* Lists
* Tuples
* Variables
* `for` loops
* `if`, `elif`, and `else`
* Type conversion using `int()` and `float()`
* Arithmetic calculations
* Accumulators
* Conditional comparisons
* Formatted strings using f-strings
* Basic aggregation
* Dictionaries

## Development Approach

The practical was developed incrementally.

I initially approached the CSV using `csv.reader`, extracting values according to their column positions. This allowed me to understand how the raw CSV data was being read before attempting to perform the required analysis.

I then built the calculations step by step, including transaction revenue, total units, category revenue, product revenue, and maximum values.

I also experimented with `csv.DictReader`. This showed me an alternative way of working with CSV data where columns can be accessed using their names rather than numerical indexes.

For example, instead of relying on a position such as:

`row[2]`

a dictionary-based approach can access the column by its name.

This was particularly useful for understanding how Python dictionaries can make data-processing programs easier to read and maintain.

## Limitations and Lessons Learned

One of the main lessons from this practical was that a program can produce useful results while still having problems with its design.

My initial solution used separate variables for each product and category. Although this worked with the supplied dataset, it created a large amount of repetitive code.

For example, adding a new product would require additional variables and additional conditional statements.

This helped me understand why data structures such as **dictionaries** are important when processing datasets where the number of products, customers, or categories can change.

I also identified some problems in my initial calculations, particularly around:

* Calculating average transaction value versus average revenue per unit.
* Aggregating revenue across multiple transactions belonging to the same customer.
* Distinguishing the highest individual transaction from the highest total customer spending.

These issues are important because they demonstrate that processing data is not only about writing code that runs—it is also about making sure the calculations represent the question being asked.

## Resources Used

The implementation was completed independently without using AI chatbots to generate the solution.

Resources used during development included:

* Python documentation
* GeeksforGeeks
* W3Schools
* Stack Overflow
* VS Code IntelliSense
* Previous knowledge and work from Practical 01

AI assistance was used for reviewing, explaining, and documenting the learning process rather than generating the implementation.

## Project Structure

```text
Practical 02/
│
├── Data/
│   └── sales.csv
│
├── main.py
├── README.md
└── AI-LEARNING-LOG.md
```

## How to Run

From the root of the `Python Projects` repository, run:

```bash
python3 "Practical 02/main.py"
```

The program reads the sales data from:

```text
Practical 02/Data/sales.csv
```

and displays the resulting analysis in the terminal.

## Next Steps

The main area I want to improve after this practical is writing programs that are less repetitive and more scalable.

In particular, I want to become more comfortable with:

* Dictionaries
* Functions
* Grouping and aggregation
* Reusable data-processing logic
* Better ways of modelling data

These areas will be developed further in the next practical.
