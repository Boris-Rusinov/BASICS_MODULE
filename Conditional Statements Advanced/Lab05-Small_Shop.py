product = input()
city = input()
quantity = float(input())

price = 0.00 #Faster to do this, instead of creating the variable in the if statements

if city == "Varna":
    if product == "coffee":
        price = quantity * 0.45
    elif product == "water":
        price = quantity * 0.70
    elif product == "beer":
        price = quantity * 1.10
    elif product == "sweets":
        price = quantity * 1.35
    elif product == "peanuts":
        price = quantity * 1.55
elif city == "Sofia":
    if product == "coffee":
        price = quantity * 0.50
    elif product == "water":
        price = quantity * 0.80
    elif product == "beer":
        price = quantity * 1.20
    elif product == "sweets":
        price = quantity * 1.45
    elif product == "peanuts":
        price = quantity * 1.60
elif city == "Plovdiv":
    if product == "coffee":
        price = quantity * 0.40
    elif product == "water":
        price = quantity * 0.70
    elif product == "beer":
        price = quantity * 1.15
    elif product == "sweets":
        price = quantity * 1.30
    elif product == "peanuts":
        price = quantity * 1.50

print(price)