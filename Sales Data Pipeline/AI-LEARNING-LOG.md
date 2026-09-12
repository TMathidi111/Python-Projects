# AI Learning Log

## Project

**Sales Data Pipeline**

## Purpose of This Log

This document records how AI was used during the development and review of this project.

The goal of the project was to develop my own programming and problem-solving ability rather than rely on AI to generate the implementation.

---

## AI Usage During Development

I did **not** use AI to generate the submitted implementation of the Sales Data Pipeline.

The implementation was developed independently using:

* Python documentation
* W3Schools
* GeeksforGeeks
* Stack Overflow
* IntelliSense and editor suggestions
* My own experimentation and debugging

When I encountered problems, I used documentation and experimentation to understand how Python features worked.

---

## AI Usage After Implementation

After completing the project, AI was used as a reviewer and tutor.

The main purposes were:

* Reviewing the completed implementation
* Identifying weaknesses in the solution
* Explaining concepts that I had not fully understood
* Comparing the implementation against the original project requirements
* Discussing how the code could become more scalable
* Explaining dictionary-based aggregation
* Explaining how dictionary keys and values work
* Understanding `.items()`, keys, and values
* Understanding how missing data affected aggregation
* Identifying concepts that should be revisited in a future project

AI was therefore used primarily for **review, explanation, and learning**, rather than for producing the submitted solution.

---

## Main Weakness Identified

The largest weakness identified during review was my understanding of **generic aggregation**.

My implementation still contained hard-coded variables such as:

```text
thabo_total
lerato_total
mpho_total
naledi_total
```

and similar variables for products and categories.

This meant that adding a new customer or product would require modifying the Python program.

The more scalable approach is to use a dictionary where the data itself becomes the key:

```python
customer_revenue = {}
```

For example:

```python
if customer not in customer_revenue:
    customer_revenue[customer] = 0

customer_revenue[customer] += transaction_revenue
```

This was an important conceptual improvement because the program can now respond to the data rather than requiring the programmer to know the data beforehand.

---

## Concepts I Need to Improve

The review identified several areas that I need to practise further:

1. Dictionary-based aggregation
2. Functions and reusable logic
3. Generic product and category aggregation
4. Data modelling using dictionaries
5. Separating validation, transformation, aggregation, and reporting
6. Dynamic analysis of aggregated data
7. Writing programs that scale when the input data changes

---

## Important Learning

One of the most useful lessons from this project was that **scalability can begin at the data-structure level**.

For example, hard-coding:

```text
Thabo
Lerato
Mpho
Naledi
```

into the program makes the code dependent on the current dataset.

Using:

```python
customer_revenue[customer]
```

allows the data to determine which customers exist.

This changed the way I think about Python dictionaries. I previously thought of them mainly as a way to store key-value information. I now understand that they can also be used as dynamic structures for grouping and aggregating data.

---

## Reflection

I consider this project successful in introducing the concepts, but not successful in mastering all of them.

The biggest gap was that I understood the idea of aggregation but continued implementing it using hard-coded variables.

Rather than simply moving on, I decided that the next project should deliberately revisit these concepts and require me to solve a different problem using the same underlying ideas.

The next project will therefore focus heavily on:

* Dictionaries
* Generic aggregation
* Functions
* Data modelling
* Validation
* Reusable processing logic
* Scalable reporting

The purpose is not simply to repeat the previous project, but to demonstrate that I can apply the concepts independently to a new problem.

---

## AI Learning Principle

AI was used as a **teacher and reviewer**, not as the programmer.

The intention of this project is to build my own ability to reason about data-processing problems, understand why a solution works, and eventually design scalable programs independently.

Future projects will continue following this approach.
