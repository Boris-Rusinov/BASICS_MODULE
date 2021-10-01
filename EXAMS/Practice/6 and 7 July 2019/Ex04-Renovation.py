from math import ceil

wall_height = int(input())
wall_width = int(input())
wall_area_not_to_be_painted_percentage = int(input())

# In total, 4 walls to paint

total_painted_area = 0
total_area_to_paint = wall_height * wall_width * 4
total_area_to_paint -= (total_area_to_paint * (wall_area_not_to_be_painted_percentage / 100))
total_area_to_paint = ceil(total_area_to_paint)
diff = 0

curr_liters_paint = input()
while True:
    if curr_liters_paint == "Tired!":
        diff = total_area_to_paint - total_painted_area
        print(f"{diff} quadratic m left.")
        break

    curr_liters_paint = int(curr_liters_paint)
    total_painted_area += curr_liters_paint

    if total_painted_area > total_area_to_paint:
        diff = total_painted_area - total_area_to_paint
        print(f"All walls are painted and you have {diff} l paint left!")
        break
    elif total_painted_area == total_area_to_paint:
        diff = total_painted_area - total_area_to_paint
        print("All walls are painted! Great job, Pesho!")
        break
    curr_liters_paint = input()