day_count = int(input())
hours_per_day = int(input())

# For every even day and odd hour parking taxes 2.50 lv.
# For every odd day and even hour parking taxes 1.25 lv.
# Every other case parking taxes 1 lv.

curr_day_total_taxes = 0.00
total_taxes = 0.00

for curr_day in range(1, day_count + 1):
    for curr_hour in range(1, hours_per_day + 1):
        if curr_day % 2 == 0 and curr_hour % 2 == 1:
            curr_day_total_taxes += 2.50
        elif curr_day % 2 == 1 and curr_hour % 2 == 0:
            curr_day_total_taxes += 1.25
        else:
            curr_day_total_taxes += 1.00

    total_taxes += curr_day_total_taxes
    print(f"Day: {curr_day} - {curr_day_total_taxes:.2f} leva")
    curr_day_total_taxes = 0

print(f"Total: {total_taxes:.2f} leva")