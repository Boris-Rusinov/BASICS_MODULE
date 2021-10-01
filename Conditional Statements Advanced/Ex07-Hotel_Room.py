month = input()
nights = int(input())

studio_price =  0.00
apartment_price =  0.00
price_of_stay_studio = 0.00
price_of_stay_apartment = 0.00

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if nights > 14:
        studio_price -= studio_price * 0.30
        apartment_price -= apartment_price * 0.10
    elif nights > 7:
        studio_price -= studio_price * 0.05
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        studio_price -= studio_price * 0.20
        apartment_price -= apartment_price * 0.10
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    if nights > 14:
        apartment_price -= apartment_price * 0.10

price_of_stay_studio = studio_price * nights
price_of_stay_apartment = apartment_price * nights

print(f"Apartment: {price_of_stay_apartment:.2f} lv.")
print(f"Studio: {price_of_stay_studio:.2f} lv.")