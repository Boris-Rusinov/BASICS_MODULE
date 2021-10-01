from math import ceil

people_count = int(input())
entrance_fee_per_person = float(input())
fee_per_lounge = float(input())
fee_per_umbrella = float(input())

total_price = 0.00

total_price_people = people_count * entrance_fee_per_person
total_price_lounges = ceil(people_count * (3/4)) * fee_per_lounge
total_price_umbrellas = ceil(people_count / 2) * fee_per_umbrella

total_price = total_price_people + total_price_lounges + total_price_umbrellas

print(f"{total_price:.2f} lv.")