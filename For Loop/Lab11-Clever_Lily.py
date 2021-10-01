lily_age = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

total_money_lily = 0
total_money_taken_brother = 0   #Cumulative money Lily's brother took from her. Because it is 1.00 lv every time, it will be equivalent to Lily's
toys_amount = 0                 #total even years
total_toys_profit = 0
curr_money_to_add = 10
diff = 0

for curr_year in range(1, lily_age + 1):
    if curr_year % 2 == 0:
        total_money_taken_brother += 1
        total_money_lily += curr_money_to_add
        curr_money_to_add += 10
    else:
        toys_amount += 1

total_toys_profit = toys_amount * price_per_toy
total_money_lily += total_toys_profit
total_money_lily -= total_money_taken_brother

diff = total_money_lily - washing_machine_price

if diff >= 0:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {abs(diff):.2f}")







