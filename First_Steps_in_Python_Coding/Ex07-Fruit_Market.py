strawberry_price = float(input())
banana_quantity = float(input())
orange_quantity = float(input())
rasberry_quantity = float(input())
strawberry_quantity = float(input())

rasberry_price = strawberry_price / 2

orange_price = rasberry_price - rasberry_price * 0.4

banana_price = rasberry_price - rasberry_price * 0.8

total_strawberry_price = strawberry_price * strawberry_quantity
total_rasberry_price = rasberry_price * rasberry_quantity
total_orange_price = orange_price * orange_quantity
total_banana_price = banana_price * banana_quantity

total_price = total_strawberry_price  + total_banana_price + total_orange_price  + total_rasberry_price

print(total_price)