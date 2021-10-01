num_to_equate = int(input())

valid_combos = 0
curr_sum = 0

x1 = 0
x2 = 0
x3 = 0

while x1 <= num_to_equate:
    while x2 <= num_to_equate:
        while x3 <= num_to_equate:
            curr_sum = x1 + x2 + x3
            if curr_sum == num_to_equate:
                valid_combos += 1
                break
            x3 += 1
        x3 = 0
        x2 += 1
    x2 = 0
    x1 += 1

print(valid_combos)