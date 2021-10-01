budget = float(input())
video_card_count = int(input())   # 250 lv. per piece
processor_count = int(input())  # 35% video card price per piece
RAM_memory_count = int(input())  # 10% video card price per piece

video_card_total_cost = video_card_count * 250
processor_total_cost = video_card_total_cost * 0.35 * processor_count
RAM_memory_total_cost = video_card_total_cost * 0.10 * RAM_memory_count
total_costs = video_card_total_cost + processor_total_cost + RAM_memory_total_cost

diff = 0.00

if video_card_count > processor_count:
    total_costs -= (total_costs * 0.15)

diff = budget - total_costs

if diff >= 0:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(diff):.2f} leva more!")