budget = float(input())

product_count = 0
curr_product_name = ""
curr_product_price = 0.00

total_expenses = 0.00
diff = 0.00

while True:
    curr_product_name = input()
    if curr_product_name == "Stop":
        print(f"You bought {product_count} products for {total_expenses:.2f} leva.")
        break

    curr_product_price = float(input())
    product_count += 1

    if product_count % 3 == 0:
        curr_product_price /= 2

    total_expenses += curr_product_price

    if total_expenses > budget:
        diff = total_expenses - budget

        print("You don't have enough money!")
        print(f"You need {diff:.2f} leva!")
        break