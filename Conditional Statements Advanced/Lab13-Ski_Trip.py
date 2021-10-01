length_of_stay = int(input())
room_type = input()
review = input()

nights_stayed = length_of_stay - 1
price_for_stay = 0.00

"""
room for one person = 18.00
apartment = 25.00
president apartment = 35.00
"""

if room_type == "room for one person":
    if length_of_stay < 10:
        price_for_stay = nights_stayed * 18
    elif  length_of_stay <= 15:
        price_for_stay = nights_stayed * 18
    else:
        price_for_stay = nights_stayed * 18
elif room_type == "apartment":
    if length_of_stay < 10:
        price_for_stay = nights_stayed * 25
        price_for_stay -= price_for_stay * 0.30
    elif  length_of_stay <= 15:
        price_for_stay = nights_stayed * 25
        price_for_stay -= price_for_stay * 0.35
    else:
        price_for_stay = nights_stayed * 25
        price_for_stay -= price_for_stay * 0.50
elif room_type == "president apartment":
    if length_of_stay < 10:
        price_for_stay = nights_stayed * 35
        price_for_stay -= price_for_stay * 0.10
    elif  length_of_stay <= 15:
        price_for_stay = nights_stayed * 35
        price_for_stay -= price_for_stay * 0.15
    else:
        price_for_stay = nights_stayed * 35
        price_for_stay -= price_for_stay * 0.20

if review == "positive":
    price_for_stay += price_for_stay * 0.25
elif review == "negative":
    price_for_stay -= price_for_stay * 0.10

print(f"{price_for_stay:.2f}")