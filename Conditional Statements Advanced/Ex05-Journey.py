budget = float(input())
season = input()

spent_money = 0.00
country_of_stay = ""
place_of_stay = ""

if budget <= 100:
    country_of_stay = "Bulgaria"
    if season == "summer":
        place_of_stay = "Camp"
        spent_money = budget * 0.30
    elif season == "winter":
        place_of_stay = "Hotel"
        spent_money = budget * 0.70
elif budget <= 1000:
    country_of_stay = "Balkans"
    if season == "summer":
        place_of_stay = "Camp"
        spent_money = budget * 0.40
    elif season == "winter":
        place_of_stay = "Hotel"
        spent_money = budget * 0.80
elif budget > 1000:
    country_of_stay = "Europe"
    place_of_stay = "Hotel"
    spent_money = budget * 0.90

print(f"Somewhere in {country_of_stay}")
print(f"{place_of_stay} - {spent_money:.2f}")
