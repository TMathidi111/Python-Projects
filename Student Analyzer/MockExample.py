marks = [78, 64, 91, 55, 43]
sum = 0
average = 0
i = 0

while i < len(marks) :
    sum += marks[i]
    i += 1
average = sum/len(marks)

max = marks[0]
min = marks[0]

for i in range(len(marks)):
    if(marks[i] > max):
        max = marks[i]
    if(marks[i] < min):
        min = marks[i]


print(f"Average marks: {average}")
print(f"Maximum mark: {max}")
print(f"Minimum mark: {min}")
