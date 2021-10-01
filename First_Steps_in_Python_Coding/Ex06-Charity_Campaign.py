campaign_duration = int(input())
confectioner_amount = int(input())
cake_amount_per_day = int(input())
waffle_amount_per_day = int(input())
pancake_amount_per_day = int(input())

cake_price_per_day = cake_amount_per_day * 45
waffle_price_pre_day = waffle_amount_per_day * 5.80
pancake_price_per_day = pancake_amount_per_day * 3.20

end_income = (cake_price_per_day + waffle_price_pre_day + pancake_price_per_day) * campaign_duration * confectioner_amount

end_income = end_income - end_income * (1/8)

print(end_income)