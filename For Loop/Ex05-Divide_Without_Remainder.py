num_amount = int(input())

p1_count = 0
p2_count = 0
p3_count = 0

p1_percentage = 0.00
p2_percentage = 0.00
p3_percentage = 0.00

for curr_index in range(0, num_amount):
    curr_num = int(input())

    if curr_num % 2 == 0:
        p1_count += 1
    if curr_num % 3 == 0:
        p2_count += 1
    if curr_num % 4 == 0:
        p3_count += 1

p1_percentage = p1_count / num_amount * 100
p2_percentage = p2_count / num_amount * 100
p3_percentage = p3_count / num_amount * 100

print(f"{p1_percentage:.2f}%")
print(f"{p2_percentage:.2f}%")
print(f"{p3_percentage:.2f}%")