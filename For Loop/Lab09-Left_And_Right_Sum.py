num_amount = int(input())

left_sum = 0
right_sum = 0
diff = 0

for curr_index in range(0, num_amount):
    left_num = int(input())
    left_sum += left_num

for curr_index in range(0, num_amount):
    right_num = int(input())
    right_sum += right_num

diff = left_sum - right_sum
if diff == 0:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {abs(diff)}")