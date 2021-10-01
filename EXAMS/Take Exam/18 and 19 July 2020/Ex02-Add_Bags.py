over_20_kgs_baggage_price = float(input())
baggage_weight_kgs = float(input())
days_till_trip = int(input())
baggage_count = int(input())

price_per_baggage = 0.00
total_baggage_price = 0.00

if baggage_weight_kgs < 10:
    price_per_baggage = over_20_kgs_baggage_price * 0.20
elif baggage_weight_kgs <= 20:
    price_per_baggage = over_20_kgs_baggage_price * 0.50
else:
    price_per_baggage = over_20_kgs_baggage_price

if days_till_trip < 7:
    price_per_baggage += price_per_baggage * 0.40
elif days_till_trip <= 30:
    price_per_baggage += price_per_baggage * 0.15
else:
    price_per_baggage += price_per_baggage * 0.10

total_baggage_price = price_per_baggage * baggage_count

print(f"The total price of bags is: {total_baggage_price:.2f} lv.")