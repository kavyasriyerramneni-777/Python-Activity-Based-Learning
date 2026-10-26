marks = [
    [80, 90, 85],
    [70, 75, 80],
    [90, 95, 92]
]

for i in range(len(marks)):
    total = sum(marks[i])
    average = total / len(marks[i])

    print("Student", i + 1)
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))