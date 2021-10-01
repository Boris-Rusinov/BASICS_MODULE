start_num_range = int(input())
end_num_range = int(input())

str_start_num = str(start_num_range)
str_end_num = str(end_num_range)

first_digit_start_num = int(str_start_num[0])
second_digit_start_num = int(str_start_num[1])
third_digit_start_num = int(str_start_num[2])
fourth_digit_start_num = int(str_start_num[3])

first_digit_end_num = int(str_end_num[0])
second_digit_end_num = int(str_end_num[1])
third_digit_end_num = int(str_end_num[2])
fourth_digit_end_num = int(str_end_num[3])

for curr_first_digit_to_check in range(first_digit_start_num, first_digit_end_num + 1):
    for curr_second_digit_to_check in range(second_digit_start_num, second_digit_end_num + 1):
        for curr_third_digit_to_check in range(third_digit_start_num, third_digit_end_num + 1):
            for curr_fourth_digit_to_check in range(fourth_digit_start_num, fourth_digit_end_num + 1):

                if curr_first_digit_to_check % 2 == 1 and curr_second_digit_to_check % 2 == 1 and curr_third_digit_to_check % 2 == 1 and curr_fourth_digit_to_check % 2 == 1:
                    print(f"{curr_first_digit_to_check}{curr_second_digit_to_check}{curr_third_digit_to_check}{curr_fourth_digit_to_check}", end=" ")