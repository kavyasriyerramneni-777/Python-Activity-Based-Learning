rows = int(input("Enter number of rows: "))
columns = int(input("Enter seats per row: "))

seat = 1

for i in range(rows):
    for j in range(columns):
        print("S" + str(seat), end="\t")
        seat += 1
    print()