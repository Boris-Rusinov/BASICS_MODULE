multiplier_a = 1
multiplier_b = 1

result = multiplier_a * multiplier_b

while multiplier_a < 11:
    while multiplier_b < 11:
        print(f"{multiplier_a} * {multiplier_b} = {result}")
        multiplier_b += 1
        result = multiplier_a * multiplier_b
    multiplier_a += 1
    multiplier_b = 1
    result = multiplier_a * multiplier_b