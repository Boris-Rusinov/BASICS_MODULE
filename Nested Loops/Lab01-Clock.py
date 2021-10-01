hours = 0
minutes = 0

while hours <= 23:
    while minutes <= 59:
        print(f"{hours}:{minutes}")
        minutes += 1
    hours += 1
    minutes = 0