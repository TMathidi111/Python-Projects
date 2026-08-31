# AI Learning Log — Practical 01

## Purpose

This document records how AI and other resources were used during the development of Student Analyzer.

The purpose is to maintain transparency about AI usage and distinguish between code that I developed myself, concepts I researched, and assistance received from AI.

---

## Starting Point

At the beginning of the practical, I had basic exposure to Python but was not yet comfortable solving programming problems independently.

The main objective was therefore not simply to produce a working program, but to practise breaking a problem into smaller computational steps.

---

## Development Process

### 1. Reading the file

I independently identified that the program needed to open the external student file.

I used:

```python
with open("Student Analyzer/Data/students.txt") as students:
```

I initially did not understand that the file object could be used directly as the source of a `for` loop.

I learned that:

```python
for line in students:
```

processes the file one line at a time.

This became one of the main learning points of the practical.

---

### 2. Parsing each student

I used resources including W3Schools and IntelliSense to understand methods such as:

```python
.strip()
.split(",")
```

I learned that a raw line such as:

```text
Thabo,78
```

could be transformed into separate values:

```text
Thabo
78
```

The important learning point was not memorising `.strip()` or `.split()`, but understanding why the raw data needed to be transformed before it could be processed.

---

### 3. Calculating the average

I initially struggled with calculating the overall average because I was thinking about one student at a time rather than maintaining information across iterations.

The solution introduced the concept of an accumulator:

```python
total += mark
```

and a counter:

```python
count += 1
```

I learned that these variables need to exist outside the loop so that information is not reset for every student.

---

### 4. Finding maximum and minimum

I implemented logic that maintains a current maximum and minimum value.

The basic reasoning was:

```text
Start with a current value
        ↓
Look at the next mark
        ↓
Compare it with the current value
        ↓
Replace it if necessary
        ↓
Continue
```

This introduced the idea of maintaining a current "best" or "worst" value while iterating through data.

---

### 5. Assigning grades

I implemented conditional logic to convert a numerical mark into a grade.

The process was:

```text
Mark
 ↓
Check range
 ↓
Assign grade
```

For example:

```text
90–100 → A
80–89  → B
70–79  → C
60–69  → D
Below 60 → F
```

I initially attempted to create another loop over a single mark. This caused an error because an integer is not iterable.

This helped reinforce the distinction between:

```text
A collection of values
```

and:

```text
One individual value
```

---

### 6. Creating the student list

I independently came up with the idea of creating:

```python
student_list = []
```

and then adding each transformed student:

```python
student_list.append((name, mark, symbol))
```

This produced a structure similar to:

```text
[
    ("Thabo", 78, "C"),
    ("Lerato", 64, "D"),
    ("Mpho", 91, "A")
]
```

I learned that this allows the program to retain the transformed records after processing them.

---

### 7. Iterating over the transformed data

I initially did not understand why the program could use:

```python
for student in student_list:
```

I learned that Python does not inherently know that the item is a "student."

The variable `student` is simply the name I chose for the current item in the collection.

Because I created each item as:

```text
(name, mark, symbol)
```

each item represents one student.

This helped me understand the general Python pattern:

```python
for item in collection:
```

where `item` represents the current element being processed.

---

## Resources Used

The following resources were used during development:

* Python documentation
* W3Schools
* IntelliSense
* AI tutoring and code review

Resources were used to understand concepts and syntax rather than to obtain a complete solution to the practical.

---

## AI's Role

AI acted primarily as a tutor and marker.

When I became stuck, AI was instructed not to immediately provide the answer. Instead, it asked questions intended to help me identify the problem myself.

For example, when I incorrectly attempted to use:

```python
sum(grade)
```

AI explained that `grade` represented one integer rather than a collection, and guided me toward understanding the need for a running total.

When I eventually requested the complete solution, AI provided it so that I could compare my reasoning against a working implementation.

AI subsequently assessed the completed practical.

---

## Assessment

Final AI assessment:

**78/100**

### Strengths

* Correct file processing
* Correct parsing of records
* Correct use of loops
* Correct statistical calculations
* Correct grade classification
* Good idea to preserve transformed records in a list
* Increasing understanding of iteration and data structures

### Areas for Improvement

* Become more independent when breaking problems into computational steps.
* Strengthen understanding of Python data structures.
* Reduce dependence on IntelliSense for constructing unfamiliar code.
* Improve ability to reason about data before writing code.

---

## Personal Reflection

The most important lesson from this practical was that programming is not primarily about memorising syntax.

The more important process is:

```text
Understand the problem
        ↓
Break it into smaller problems
        ↓
Determine what information must be stored
        ↓
Determine what needs to happen to each piece of data
        ↓
Use Python constructs to implement the reasoning
```

I also learned that using documentation and development tools is not necessarily a problem. The important distinction is whether I understand the code I use and why it solves the problem.

This practical established the approach I will use for future Python projects.
