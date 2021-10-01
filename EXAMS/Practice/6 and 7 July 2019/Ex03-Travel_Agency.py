city = input()
packet_type = input()
possession_of_VIP_discount = input()
days = int(input())
is_valid = True

price_per_day = 0.00
total_stay_cost = 0.00

if days < 1:
    is_valid = False
    print("Days must be positive number!")

if city == "Bansko" or city == "Borovets":
    if packet_type == "noEquipment":
        price_per_day = 80
        if possession_of_VIP_discount == "yes":
            price_per_day -= price_per_day * 0.05
    elif packet_type == "withEquipment":
        price_per_day = 100
        if possession_of_VIP_discount == "yes":
            price_per_day -= price_per_day * 0.10
    else:
        is_valid = False
        print("Invalid input!")
elif city == "Varna" or city == "Burgas":
    if packet_type == "noBreakfast":
        price_per_day = 100
        if possession_of_VIP_discount == "yes":
            price_per_day -= price_per_day * 0.07
    elif packet_type == "withBreakfast":
        price_per_day = 130
        if possession_of_VIP_discount == "yes":
            price_per_day -= price_per_day * 0.12
    else:
        is_valid = False
        print("Invalid input!")
else:
    is_valid = False
    print("Invalid input!")

if is_valid:

    if days > 7:
        days -= 1

    total_stay_cost += price_per_day * days
    print(f"The price is {total_stay_cost:.2f}lv! Have a nice time!")