num_amount = int(input())

p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

p1_percentage = 0.00
p2_percentage = 0.00
p3_percentage = 0.00
p4_percentage = 0.00
p5_percentage = 0.00

for curr_index in range(0, num_amount):
    curr_num = int(input())
    if curr_num < 200:
        p1_count += 1
    elif curr_num < 400:
        p2_count += 1
    elif curr_num < 600:
        p3_count += 1
    elif curr_num < 800:
        p4_count += 1
    else:
        p5_count += 1

p1_percentage = p1_count / num_amount * 100
p2_percentage = p2_count / num_amount * 100
p3_percentage = p3_count / num_amount * 100
p4_percentage = p4_count / num_amount * 100
p5_percentage = p5_count / num_amount * 100

print(f"{p1_percentage:.2f}%")
print(f"{p2_percentage:.2f}%")
print(f"{p3_percentage:.2f}%")
print(f"{p4_percentage:.2f}%")
print(f"{p5_percentage:.2f}%")