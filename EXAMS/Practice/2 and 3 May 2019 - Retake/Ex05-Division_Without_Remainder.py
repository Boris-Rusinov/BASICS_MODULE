num_count = int(input())

nums_divisible_by_2_percentage = 0.00
nums_divisible_by_3_percentage = 0.00
nums_divisible_by_4_percentage = 0.00

curr_num = 0

for curr_index in range(0, num_count):
    curr_num = int(input())

    if curr_num % 2 == 0:
        nums_divisible_by_2_percentage += 1

    if curr_num % 3 == 0:
        nums_divisible_by_3_percentage += 1

    if curr_num % 4 == 0:
        nums_divisible_by_4_percentage += 1

nums_divisible_by_2_percentage = nums_divisible_by_2_percentage / num_count * 100
nums_divisible_by_3_percentage = nums_divisible_by_3_percentage / num_count * 100
nums_divisible_by_4_percentage = nums_divisible_by_4_percentage / num_count * 100

print(f"{nums_divisible_by_2_percentage:.2f}%")
print(f"{nums_divisible_by_3_percentage:.2f}%")
print(f"{nums_divisible_by_4_percentage:.2f}%")