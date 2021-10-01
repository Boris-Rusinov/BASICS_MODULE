hall_rent = int(input())

cake_price = hall_rent * 0.2

drinks_price = cake_price  - cake_price * 0.45

animator_price = hall_rent * (1/3)

total_price = hall_rent + cake_price + drinks_price + animator_price

print(total_price)