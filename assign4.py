subjects = ["Python", "Maths", "English"]

for subject in subjects:
    first = int(input("Enter " + subject + " first exam marks: "))
    second = int(input("Enter " + subject + " second exam marks: "))

    difference = second - first

    if difference > 0:
        print(subject, "Improved by", difference, "marks")
    elif difference < 0:
        print(subject, "Decreased by", -difference, "marks")
    else:
        print(subject, "No change")