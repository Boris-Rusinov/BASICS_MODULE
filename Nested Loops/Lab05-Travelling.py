"""
curr_destination_name = input()
curr_destination_min_price = float(input())

is_num = False
is_min_price = False
gone_to_destination = False
curr_saved_money = 0
curr_money_to_add = 0

#Will assume that every Destination/Min Budget iteration is separate, with no carry over of previous saved money

while True:
    command = input()
    is_num = command.isnumeric()

    if is_num == False:
        if command == "End":
            break
        else:
            curr_destination_name = command
            gone_to_destination = False
    else:
        if is_min_price == False:
            curr_money_to_add = float(command)
            curr_destination_min_price -= curr_money_to_add
            if curr_destination_min_price <= 0 and gone_to_destination == False:
                print(f"Going to {curr_destination_name}!")
                is_min_price = True
                gone_to_destination = True
        else:
            curr_destination_min_price = float(command)
            is_min_price = False
"""

curr_destination_name = input()
#curr_destination_min_price = float(input())
curr_saved_money = 0
curr_money_to_add = 0

while True:
    if curr_destination_name == "End":
        break

    curr_destination_min_price = float(input())
    while curr_saved_money < curr_destination_min_price:
        curr_money_to_add = float(input())
        curr_saved_money += curr_money_to_add
    print(f"Going to {curr_destination_name}!")
    curr_destination_name = input()
    curr_saved_money = 0