trip_price = float(input())
puzzles_amount = int(input())
talking_dolls_amount = int(input())
stuffed_bears_amount = int(input())
minions_amount = int(input())
toy_trucks_amount = int(input())

puzzles_price = puzzles_amount * 2.60
talking_dolls_price = talking_dolls_amount * 3
stuffed_bears_price = stuffed_bears_amount * 4.10
minions_price = minions_amount * 8.20
toy_trucks_price = toy_trucks_amount * 2

total_price = puzzles_price + talking_dolls_price + stuffed_bears_price + minions_price + toy_trucks_price

total_toy_amount = puzzles_amount + talking_dolls_amount + stuffed_bears_amount + minions_amount + toy_trucks_amount

if(total_toy_amount >= 50):
    total_price -= total_price * 0.25

total_price -= total_price * 0.10

if(total_price >= trip_price):
    print(f"Yes! {total_price - trip_price:.2f} lv left.")
elif(total_price < trip_price):
    print(f"Not enough money! {trip_price - total_price:.2f} lv needed.")