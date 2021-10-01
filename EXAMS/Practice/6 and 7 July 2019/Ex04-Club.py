needed_profit = float(input())

curr_drink_price = 0
curr_drink_count = 0
curr_order_profit = 0.00
total_profit = 0.00
diff = 0.00

drink_name = input()
while True:
    if drink_name == "Party!":
        diff = needed_profit - total_profit
        print(f"We need {diff:.2f} leva more.")
        print(f"Club income - {total_profit:.2f} leva.")
        break

    curr_drink_count = int(input())
    curr_drink_price = len(drink_name)
    curr_order_profit = curr_drink_count * curr_drink_price

    if curr_order_profit % 2 != 0:
        curr_order_profit -= curr_order_profit * 0.25

    total_profit += curr_order_profit

    if total_profit >= needed_profit:
        print("Target acquired.")
        print(f"Club income - {total_profit:.2f} leva.")
        break

    drink_name = input()