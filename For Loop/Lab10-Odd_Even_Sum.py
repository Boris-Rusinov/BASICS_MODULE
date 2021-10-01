num_amount = int(input())

even_sum = 0
odd_sum = 0
diff = 0

for curr_index in range(0, num_amount):
    curr_num = int(input())

    if curr_index % 2 == 0:
        even_sum += curr_num
    elif curr_index % 2 == 1:
        odd_sum += curr_num

diff = even_sum - odd_sum
if diff == 0:
    print(f"Yes")
    print(f"Sum = {even_sum}")
else:
    print(f"No")
    print(f"Diff = {abs(diff)}")