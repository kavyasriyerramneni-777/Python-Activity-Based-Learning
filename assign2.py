total = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))

percentage = attended / total * 100

print("Attendance:", percentage, "%")

if percentage >= 75:
    print("Eligible for examination")
else:
    needed = 0
    while (attended + needed) / (total + needed) * 100 < 75:
        needed += 1

    print("Not eligible")
    print("Classes needed:", needed)