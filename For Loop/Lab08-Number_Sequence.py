import sys

num_amount = int(input())

largest_num = -sys.maxsize
smallest_num = sys.maxsize

for curr_index in range(0, num_amount):
    curr_num = int(input())

    if curr_num > largest_num:
        largest_num = curr_num
    if curr_num < smallest_num:
        smallest_num = curr_num

print(f"Max number: {largest_num}")
print(f"Min number: {smallest_num}")
