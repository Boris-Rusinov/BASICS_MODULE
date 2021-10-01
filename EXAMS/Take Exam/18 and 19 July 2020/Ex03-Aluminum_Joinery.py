joinery_count = int(input())
joinery_type = input()
shipment_method = input()

if joinery_count < 10:
    print("Invalid order")
else:
    price_per_joinery = 0.00
    order_total_cost = 0.00

    if joinery_type == "90X130":
        price_per_joinery = 110
        order_total_cost = joinery_count * price_per_joinery
        if joinery_count > 60:
            order_total_cost -= order_total_cost * 0.08
        elif joinery_count > 30:
            order_total_cost -= order_total_cost * 0.05
    elif joinery_type == "100X150":
        price_per_joinery = 140
        order_total_cost = joinery_count * price_per_joinery
        if joinery_count > 80:
            order_total_cost -= order_total_cost * 0.10
        elif joinery_count > 30:
            order_total_cost -= order_total_cost * 0.06
    elif joinery_type == "130X180":
        price_per_joinery = 190
        order_total_cost = joinery_count * price_per_joinery
        if joinery_count > 50:
            order_total_cost -= order_total_cost * 0.12
        elif joinery_count > 20:
            order_total_cost -= order_total_cost * 0.07
    elif joinery_type == "200X300":
        price_per_joinery = 250
        order_total_cost = joinery_count * price_per_joinery
        if joinery_count > 50:
            order_total_cost -= order_total_cost * 0.14
        elif joinery_count > 25:
            order_total_cost -= order_total_cost * 0.09

    if shipment_method == "With delivery":
        order_total_cost += 60

    if joinery_count > 99:
        order_total_cost -= order_total_cost * 0.04

    print(f"{order_total_cost:.2f} BGN")