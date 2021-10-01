film_budget = float(input())
extras = int(input())
costume_price_per_extra = float(input())

film_decor = film_budget * 0.1

if(extras > 150):
    costume_price_per_extra -= costume_price_per_extra * 0.1

film_budget -= (extras * costume_price_per_extra + film_decor)

if(film_budget >= 0):
    print("Action!")
    print(f"Wingard starts filming with {film_budget:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(film_budget):.2f} leva more.")
