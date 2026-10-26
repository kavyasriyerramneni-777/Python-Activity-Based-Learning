distance = float(input("Enter distance in km: "))
mileage = float(input("Enter mileage in km/litre: "))
price = float(input("Enter fuel price per litre: "))

fuel = distance / mileage
cost = fuel * price

print("Fuel Required:", round(fuel, 2), "litres")
print("Journey Cost:", round(cost, 2))

if cost <= 1000:
    print("Journey is within budget")
else:
    print("Journey exceeds budget")