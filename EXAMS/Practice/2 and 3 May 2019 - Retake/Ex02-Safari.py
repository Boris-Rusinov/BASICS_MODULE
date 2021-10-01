budget = float(input())
needed_liters_fuel = float(input())     # 2.10 lv. per litre
day_of_week = input()                   # 10% discount on Saturday and 20% on Sunday

# Fee for guide => 100 lv.

total_fuel_costs = needed_liters_fuel * 2.10
total_expenses = total_fuel_costs + 100
diff = 0.00

if day_of_week == "Saturday":
    total_expenses -= total_expenses * 0.10
elif day_of_week == "Sunday":
    total_expenses -= total_expenses * 0.20

diff = budget - total_expenses

if diff >= 0:
    print(f"Safari time! Money left: {diff:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {abs(diff):.2f} lv.")

