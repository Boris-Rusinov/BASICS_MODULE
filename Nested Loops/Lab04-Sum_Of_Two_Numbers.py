interval_start = int(input())
interval_end = int(input())
magic_num = int(input())

curr_outer_num = interval_start
curr_inner_num = interval_start
curr_combo_num = 0
curr_sum = 0

while curr_outer_num <= interval_end:
    while curr_inner_num <= interval_end:
        curr_sum = (curr_outer_num + curr_inner_num)
        curr_combo_num += 1
        if curr_sum == magic_num:
            print(f"Combination N:{curr_combo_num} ({curr_outer_num} + {curr_inner_num} = {curr_sum})")
            break
        curr_inner_num += 1
    if curr_sum == magic_num:
        break
    curr_outer_num += 1
    curr_inner_num = interval_start

if curr_sum != magic_num:
    print(f"{curr_combo_num} combinations - neither equals {magic_num}")