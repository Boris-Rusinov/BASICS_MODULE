num = int(input())

for first_num in range(1, 10):
    for second_num in range(1, 10):
        for third_num in range(1, 10):
            for fourth_num in range(1, 10):
                if num % first_num == 0 and num % second_num == 0 and num % third_num == 0 and num % fourth_num == 0:
                    print(f"{first_num}{second_num}{third_num}{fourth_num}", end=" ")




"""
Alternate, a lot more complicated and slower ways to do this...... Why? Why do I try to do so goddamned complicated and convoluted solutions sometimes?! Especially if there's comically easier wasy to do this? Fuck. 


from math import floor

num_to_divide = int(input())

is_no_remainder = False
is_zero_present = False
curr_magic_num = 0
curr_digit = 0
curr_division = 0
curr_num_no_changes = 0

for curr_num in range(1111, 10000):
    curr_num_no_changes = curr_num

    while True:

        if curr_num == 0:
            break

        curr_digit = curr_num % 10
        curr_num = floor(curr_num / 10)

        if curr_digit == 0:
            is_zero_present = True
            break
        else:
            is_zero_present = False

        curr_division = num_to_divide % curr_digit
        if curr_division == 0:
            is_no_remainder = True
        else:
            is_no_remainder = False
            break

                            "
                            num_to_str = str(curr_num)
                            for index, digit in enumerate(num_to_str):
                                curr_digit = int(digit)
                                if curr_digit == 0:
                                    is_zero_present = True
                                    break
                                else:
                                    is_zero_present = False
                
                                curr_division = num_to_divide % curr_digit
                                if curr_division == 0:
                                    is_no_remainder = True
                                else:
                                    is_no_remainder = False
                                    break
                            "
                    
                    
    curr_num = curr_num_no_changes

    if is_no_remainder == True and is_zero_present == False:
        curr_magic_num = curr_num
        print(curr_magic_num, end=" ")
"""




