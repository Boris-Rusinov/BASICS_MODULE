num = int(input())

current_row_num = 1
is_curr_num_bigger_than_input_num = False

for col in range(1, num + 1):
    for row in range(0, col):
        if current_row_num > num:
            is_curr_num_bigger_than_input_num = True
            break
        print(current_row_num, end=" ")
        current_row_num += 1
    if is_curr_num_bigger_than_input_num:
        break
    print()