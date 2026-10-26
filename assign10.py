prepared = int(input("Enter meals prepared: "))
served = int(input("Enter meals served: "))

if prepared > 0 and 0 <= served <= prepared:
    waste = prepared - served
    percentage = waste / prepared * 100

    print("Meals Wasted:", waste)
    print("Waste Percentage:", round(percentage, 2), "%")

    if percentage > 20:
        print("High food waste")
    else:
        print("Food waste is acceptable")
else:
    print("Invalid input")