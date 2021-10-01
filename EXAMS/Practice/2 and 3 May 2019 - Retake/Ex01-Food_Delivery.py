chicken_menu_count = int(input())      # 10.35 lv. per menu
fish_menu_count = int(input())         # 12.40 lv. per menu
vegetarian_menu_count = int(input())   # 8.15 lv. per menu

# Dessert 20% of total order price without delivery price
# Delivery price 2.50

menu_total_price = chicken_menu_count * 10.35 + fish_menu_count * 12.40 + vegetarian_menu_count * 8.15
dessert_price = menu_total_price * 0.20

order_price = menu_total_price + dessert_price + 2.50

print(f"Total: {order_price:.2f}")