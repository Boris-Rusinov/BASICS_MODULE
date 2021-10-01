group_budget = int(input())
season = input()
fishermen_count = int(input())

boat_rent = 0.00

is_valid = fishermen_count % 2 == 0

if season == "Summer":
    boat_rent = 4200
    if fishermen_count <= 6:
        boat_rent -= boat_rent * 0.10
    elif fishermen_count <= 11:
        boat_rent -= boat_rent * 0.15
    else:
        boat_rent -= boat_rent * 0.25
    if is_valid:
        boat_rent -= boat_rent * 0.05
elif season == "Autumn":
    boat_rent = 4200
    if fishermen_count <= 6:
        boat_rent -= boat_rent * 0.10
    elif fishermen_count <= 11:
        boat_rent -= boat_rent * 0.15
    else:
        boat_rent -= boat_rent * 0.25
elif season == "Winter":
    boat_rent = 2600
    if fishermen_count <= 6:
        boat_rent -= boat_rent * 0.10
    elif fishermen_count <= 11:
        boat_rent -= boat_rent * 0.15
    else:
        boat_rent -= boat_rent * 0.25
    if is_valid:
        boat_rent -= boat_rent * 0.05
elif season == "Spring":
    boat_rent = 3000
    if fishermen_count <= 6:
        boat_rent -= boat_rent * 0.10
    elif fishermen_count <= 11:
        boat_rent -= boat_rent * 0.15
    else:
        boat_rent -= boat_rent * 0.25
    if is_valid:
        boat_rent -= boat_rent * 0.05

group_budget -= boat_rent

if group_budget >= 0:
    print(f"Yes! You have {group_budget:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(group_budget):.2f} leva.")