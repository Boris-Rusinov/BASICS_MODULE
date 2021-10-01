drink_name = input()
sugar_type = input()
amount_drinks = int(input())

price_per_drink = 0.00
drinks_total_cost = 0.00

if drink_name == "Espresso":
    if sugar_type == "Without":
        price_per_drink = 0.90
        price_per_drink -= price_per_drink * 0.35
    elif sugar_type == "Normal":
        price_per_drink = 1.00
    elif sugar_type == "Extra":
        price_per_drink = 1.20
elif drink_name == "Cappuccino":
    if sugar_type == "Without":
        price_per_drink = 1.00
        price_per_drink -= price_per_drink * 0.35
    elif sugar_type == "Normal":
        price_per_drink = 1.20
    elif sugar_type == "Extra":
        price_per_drink = 1.60
elif drink_name == "Tea":
    if sugar_type == "Without":
        price_per_drink = 0.50
        price_per_drink -= price_per_drink * 0.35
    elif sugar_type == "Normal":
        price_per_drink = 0.60
    elif sugar_type == "Extra":
        price_per_drink = 0.70

if drink_name == "Espresso" and amount_drinks >= 5:
    price_per_drink -= price_per_drink * 0.25

drinks_total_cost += amount_drinks * price_per_drink

if drinks_total_cost > 15:
    drinks_total_cost -= drinks_total_cost * 0.20

print(f"You bought {amount_drinks} cups of {drink_name} for {drinks_total_cost:.2f} lv.")