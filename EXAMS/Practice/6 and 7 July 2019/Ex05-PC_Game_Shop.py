sold_games_count = int(input())

hearthstone_sales_percentage = 0.00
fornite_sales_percentage = 0.00
overwatch_sales_percentage = 0.00
others_sales_percentage = 0.00

game_name = ""

for curr_game in range(0, sold_games_count):
    game_name = input()

    if game_name == "Hearthstone":
        hearthstone_sales_percentage += 1
    elif game_name == "Fornite":
        fornite_sales_percentage += 1
    elif game_name == "Overwatch":
        overwatch_sales_percentage += 1
    else:
        others_sales_percentage += 1

hearthstone_sales_percentage = hearthstone_sales_percentage / sold_games_count * 100
fornite_sales_percentage = fornite_sales_percentage / sold_games_count * 100
overwatch_sales_percentage = overwatch_sales_percentage / sold_games_count * 100
others_sales_percentage = others_sales_percentage / sold_games_count * 100

print(f"Hearthstone - {hearthstone_sales_percentage:.2f}%")
print(f"Fornite - {fornite_sales_percentage:.2f}%")
print(f"Overwatch - {overwatch_sales_percentage:.2f}%")
print(f"Others - {others_sales_percentage:.2f}%")