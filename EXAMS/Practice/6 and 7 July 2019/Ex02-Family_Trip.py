budget = float(input())
nights_count = int(input())
price_per_night = float(input())
additional_expenses_percentage = int(input())   #How much of the current budget is used for other, additional, expenses

additional_expenses_money = budget * (additional_expenses_percentage / 100)
stay_total_cost = 0.00
diff = 0.00

if nights_count > 7:
    price_per_night -= (price_per_night * 0.05)

stay_total_cost += price_per_night * nights_count + additional_expenses_money

diff = budget - stay_total_cost

if diff >= 0:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{abs(diff):.2f} leva needed.")

