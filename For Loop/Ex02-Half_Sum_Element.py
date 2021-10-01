import sys

num_amount = int(input())

largest_num = -sys.maxsize
sum = 0
diff = 0
for num in range(0, num_amount):
    curr_num = int(input())

    if curr_num > largest_num:
        largest_num = curr_num

    sum += curr_num

diff = sum - largest_num

if diff == largest_num:
    print("Yes")
    print(f"Sum = {largest_num}")
else:
    print("No")
    print(f"Diff = {abs(largest_num - diff)}")