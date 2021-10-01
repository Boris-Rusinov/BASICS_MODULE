duration_of_contract = input()
type_of_contract = input()
added_mobile_internet = input()
amount_of_months_to_pay = int(input())

total_cost_of_contract = 0.00

if duration_of_contract == "one":
    if type_of_contract == "Small":
        total_cost_of_contract = 9.98
    elif type_of_contract == "Middle":
        total_cost_of_contract = 18.99
    elif type_of_contract == "Large":
        total_cost_of_contract = 25.98
    elif type_of_contract == "ExtraLarge":
        total_cost_of_contract = 35.99
elif duration_of_contract == "two":
    if type_of_contract == "Small":
        total_cost_of_contract = 8.58
    elif type_of_contract == "Middle":
        total_cost_of_contract = 17.09
    elif type_of_contract == "Large":
        total_cost_of_contract = 23.59
    elif type_of_contract == "ExtraLarge":
        total_cost_of_contract = 31.79

if added_mobile_internet == "yes":
    if total_cost_of_contract <= 10:
        total_cost_of_contract += 5.50
    elif total_cost_of_contract <= 30:
        total_cost_of_contract += 4.35
    else:
        total_cost_of_contract += 3.85

if duration_of_contract == "two":
    total_cost_of_contract -= total_cost_of_contract * 0.0375

total_cost_of_contract *= amount_of_months_to_pay

print(f"{total_cost_of_contract:.2f} lv.")