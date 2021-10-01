flower_type = input()
flower_count = int(input())
budget = int(input())

price = 0.00

if flower_type == "Roses":
    price = flower_count * 5
    if flower_count > 80:
        price -= price * 0.10
elif flower_type == "Dahlias":
    price = flower_count * 3.80
    if flower_count > 90:
        price -= price * 0.15
elif flower_type == "Tulips":
    price = flower_count * 2.80
    if flower_count > 80:
        price -= price * 0.15
elif flower_type == "Narcissus":
    price = flower_count * 3
    if flower_count < 120:
        price += price * 0.15
elif flower_type == "Gladiolus":
    price = flower_count * 2.50
    if flower_count < 80:
        price += price * 0.20

budget -= price

if(budget >= 0):
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(budget):.2f} leva more.")