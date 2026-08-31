with open("Student Analyzer/Data/students.txt") as students :
    total = 0
    count = 0 
    maximum = 0 
    minimum = 100
    student_list = []

    

    for line in students : 
        student = line.strip().split(",")

        name = student[0]
        mark = int(student[1])

        total += mark 
        count += 1

        if mark > maximum: 
            maximum = mark 

        if mark < minimum:
            minimum = mark 

        
        if 90 <= mark<= 100:
            symbol = "A"
        elif 80 <= mark < 90:
            symbol = "B"
        elif 70 <= mark< 80:
            symbol = "C"
        elif 60 <= mark < 70:
            symbol = "D"
        else:
            symbol = "F"

        student_list.append((name, mark, symbol))
    
    average = total/count 

    print("STUDENT PERFORMANCE ANALYZER")
    print ("Name     Mark     Grade")
    print("----------------------------")
    for student in student_list: #take each item from student_list and temporarily store it as a student
        print(f"{student[0]}     {student[1]}     {student[2]}") #student[0] is where we stored the name value, same convention for grade and symbol
    print(f"Students analysed: {count}")
    print(f"Average mark: {average:.2f}")
    print(f"Maximum mark: {maximum}")
    print(f"Minimum mark: {minimum}")
# First ever data model, raw data from the student.txt file has been successfully transformed