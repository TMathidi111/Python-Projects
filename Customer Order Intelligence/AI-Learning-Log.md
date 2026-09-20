
```markdown
# AI Learning Log – Customer Order Intelligence

## Project

Customer Order Intelligence

## Purpose

This document records how AI and other online resources were used during the development of the Customer Order Intelligence project.

The purpose of using these resources was to understand programming concepts, troubleshoot problems and review my own implementation. I did not use AI to generate the complete project solution.

My main goal was to understand the logic behind the code rather than simply producing code that works.

---

## Development Approach

I attempted to develop the project myself and used external resources when I encountered concepts or problems that I did not fully understand.

The resources I used included:

- ChatGPT
- W3Schools
- Stack Overflow
- GeeksForGeeks
- Python documentation where required

I used these resources as references while developing and debugging the project.

---

## Use of ChatGPT

ChatGPT was used primarily as a learning and review resource.

It helped me discuss:

- Dictionary structures.
- Nested dictionaries.
- Data modelling.
- Validation approaches.
- Python errors.
- Aggregation concepts.
- Possible approaches to analysing dictionary data.

I did not ask ChatGPT to generate the complete project.

One section of my implementation was based on an approach suggested by ChatGPT:

```python
if customer not in customer_data:
    customer_data[customer] = {
        "Name": customer,
        "revenue": 0,
        "units": 0,
        "transactions": 0
    }