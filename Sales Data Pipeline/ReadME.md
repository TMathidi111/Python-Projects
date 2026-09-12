# Sales Data Pipeline

## Overview

The **Sales Data Pipeline** is a Python-based data processing project that reads sales information from a CSV file, validates the data, performs basic transformations, aggregates sales information, and produces a summary report.

This project was designed to build on the concepts introduced in the previous sales analysis project, particularly working with CSV files and processing records programmatically.

The main focus of this project was to begin thinking about how a data pipeline handles real-world data rather than assuming that every record is clean and valid.

---

## Project Objectives

The project was designed to practise:

* Reading structured data from CSV files
* Using `csv.DictReader`
* Extracting values from dictionary-based records
* Validating input data
* Handling invalid transactions
* Converting strings into appropriate data types
* Calculating transaction revenue
* Aggregating data by customer, product, and category
* Using dictionaries to store dynamic data
* Identifying useful business statistics
* Producing a readable console report
* Writing code that can work with changing data rather than relying on hard-coded values

---

## Project Structure

```text
Sales Data Pipeline/
│
├── Data/
│   └── sales_raw.csv
│
├── main.py
├── README.md
└── AI-LEARNING-LOG.md
```

---

## Input Data

The project uses a CSV file containing sales transactions.

Each transaction contains:

* Transaction ID
* Date
* Product
* Category
* Quantity
* Unit Price
* Customer

The dataset intentionally contains several problematic records, including:

* Missing quantities
* Negative prices
* Invalid quantities
* Missing customer information
* Duplicate transaction IDs

This was done to simulate the type of imperfect data that a real data-processing system may encounter.

---

## Data Processing

The program processes each CSV record individually.

The general pipeline is:

```text
CSV File
   ↓
DictReader
   ↓
Read individual transaction
   ↓
Validate data
   ↓
Reject invalid transactions
   ↓
Transform valid values
   ↓
Calculate transaction revenue
   ↓
Aggregate information
   ↓
Analyse results
   ↓
Generate report
```

---

## Validation

Transactions are checked before being included in the calculations.

The project checks for issues such as:

* Invalid quantity values
* Missing quantity values
* Invalid prices
* Invalid price values
* Missing customer information
* Duplicate transaction IDs

Invalid transactions should not contribute to the final sales calculations.

The `continue` statement is used to skip invalid records and move to the next transaction.

---

## Aggregation

One of the most important concepts introduced in this project was **dynamic aggregation using dictionaries**.

Instead of creating separate variables for every customer, product, or category, a dictionary can dynamically store the results.

For example:

```python
customer_revenue = {}

if customer not in customer_revenue:
    customer_revenue[customer] = 0

customer_revenue[customer] += transaction_revenue
```

This approach means that the program does not need to know the names of the customers in advance.

If a new customer appears in the dataset, the dictionary can automatically create a new entry for that customer.

This is an important step toward writing scalable data-processing programs.

---

## Key Learning Outcome

The most important lesson from this project was the difference between **hard-coded aggregation** and **generic aggregation**.

A hard-coded approach might require:

```text
thabo_total
lerato_total
mpho_total
naledi_total
```

A dictionary-based approach can instead represent the same concept as:

```text
customer → revenue
```

This allows the program to work with an unknown number of customers.

The same principle can be applied to:

```text
product → revenue
category → revenue
customer → transactions
customer → units
```

This introduced an important data-engineering concept: **structuring data so that the program can scale with the data instead of scaling with the programmer's code.**

---

## Limitations

Although the project achieved several of its objectives, the implementation was not as generic or reusable as originally intended.

The main limitations identified during review were:

* Some customer aggregation remained hard-coded.
* Product aggregation remained hard-coded.
* Category aggregation remained hard-coded.
* Several `if/elif` blocks could have been replaced with dictionary
