projection_type = input()
rows = int(input())
columns = int(input())

total_full_room_income = 0.00
total_seat_count = rows * columns

if projection_type == "Premiere":
    total_full_room_income = total_seat_count * 12.00
elif projection_type == "Normal":
    total_full_room_income = total_seat_count * 7.50
elif projection_type == "Discount":
    total_full_room_income = total_seat_count * 5.00

print(f"{total_full_room_income:.2f} leva")