# AI Learning Log — Practical 02

## Practical

**Practical 02 — Sales Data Analyzer**

## AI Usage

AI was **not used to generate the implementation of this practical**.

The Python solution was developed independently. I used normal development and research resources such as Python documentation, GeeksforGeeks, W3Schools, Stack Overflow, and VS Code IntelliSense when I needed help understanding a concept or writing repetitive code.

AI was used separately to help with **reviewing the work, identifying weaknesses, explaining concepts, and producing the documentation for this practical**.

This distinction is important because the purpose of the Python Projects repository is to develop my own programming and problem-solving ability rather than relying on AI to produce solutions.

---

## What I Learned

The main focus of Practical 02 was moving from processing a simple text file to working with structured CSV data.

I learned how Python can read a CSV file row by row and how the values initially come into Python as strings.

For example, values such as quantity and price need to be converted into numerical types before they can be used in calculations.

I also learned how to calculate derived information from raw data. In this practical, transaction revenue was calculated from:

```text
quantity × unit price
```

I then used accumulators and conditional statements to calculate totals and identify maximum values.

---

## CSV Reading

I initially used `csv.reader` to process the file.

This helped me understand the relationship between the CSV headers and the position of each value within a row.

For example, I could access the product using its column position.

However, this approach also made me realise that numerical indexes can make code harder to understand.

I experimented with `csv.DictReader`, which represents each row using column names. This was an important introduction to dictionaries and made me interested in learning more about them.

---

## Problem Solving

One of the biggest differences between Practical 01 and Practical 02 was the amount of information that needed to be processed.

Instead of simply calculating statistics from a small list of values, I had to think about:

1. Reading every transaction.
2. Extracting the required fields.
3. Converting numerical values.
4. Calculating transaction revenue.
5. Adding values to totals.
6. Grouping information by categories and products.
7. Comparing values to identify the largest results.
8. Presenting the results clearly.

This helped me understand a general pattern that occurs when working with datasets:

```text
Read data
    ↓
Extract data
    ↓
Transform data
    ↓
Calculate
    ↓
Aggregate
    ↓
Analyse
    ↓
Report
```

---

## What I Struggled With

The biggest difficulty was understanding how to organise information that belongs to different products, categories, and customers.

My first approach used individual variables for different products and categories.

This allowed me to solve the problem, but it resulted in a lot of repetitive code.

For example, each product needed its own variable and conditional logic.

This made me realise that my solution was designed around the specific dataset rather than around the general problem.

If another product was added to the CSV file, I would have to manually modify the program.

---

## Dictionaries

I attempted to use dictionaries with `csv.DictReader`.

I did not fully replace my original implementation with dictionaries, but experimenting with them helped me understand that dictionaries can be useful when information needs to be associated with a particular key.

This is an area I want to develop further because it appears to be much more suitable for problems involving:

* Products
* Customers
* Categories
* Counts
* Totals
* Grouped data

---

## Mistakes Identified During Review

After completing the practical, I identified several issues in my implementation.

### 1. Average Transaction Value

I initially calculated:

```text
total revenue / total units sold
```

This actually represents the average revenue per unit.

The average transaction value should instead be based on:

```text
total revenue / number of transactions
```

This showed me the importance of understanding exactly what a statistic represents rather than simply finding a formula that produces a number.

### 2. Highest-Spending Customer

My original logic compared the revenue from individual transactions and assigned the customer from the highest transaction as the highest-spending customer.

This does not necessarily identify the customer who spent the most overall.

A customer may have many smaller transactions that collectively exceed another customer's single large transaction.

The correct approach requires accumulating revenue for each customer before comparing the totals.

### 3. Highest-Value Transaction

My final output used the highest customer-related value rather than independently tracking the highest individual transaction.

This reinforced the importance of keeping different analytical concepts separate.

---

## Development Resources

The following resources were used during development:

* Python documentation
* GeeksforGeeks
* W3Schools
* Stack Overflow
* VS Code IntelliSense
* Previous Practical 01 work

I used these resources to research concepts, understand errors, and assist with repetitive coding.

I did not use an AI chatbot to generate the implementation.

---

## Reflection

Practical 02 showed me that knowing Python syntax is not enough to solve a data problem efficiently.

I was able to make the program work using variables, loops, conditions, and calculations, but the solution became repetitive as soon as I had to deal with multiple products and categories.

This was useful because it exposed a gap in my understanding rather than hiding it.

The main lesson I am taking from this practical is:

> A solution that works is not necessarily a well-designed solution.

I now need to become better at choosing appropriate data structures and designing reusable logic instead of creating separate code for every possible value.

The next stage of my learning will therefore focus on dictionaries, functions, aggregation, and better ways of structuring data-processing programs.

---

## AI Disclosure

AI was used to assist with the **review and documentation of this learning process**.

The implementation of the practical was completed independently by me. The purpose of the project is to ensure that I develop the ability to solve programming problems myself while using AI as a tool for reflection, explanation, and feedback rather than as a replacement for problem solving.
