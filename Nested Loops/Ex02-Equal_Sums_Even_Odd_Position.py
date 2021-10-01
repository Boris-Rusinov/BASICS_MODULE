from math import floor

range_min_num = int(input())
range_max_num = int(input())

curr_num_no_changes = 0

curr_even_sum = 0
curr_odd_sum = 0
curr_position = 0

for curr_num in range(range_min_num, range_max_num + 1):

    # Did this with a while loop just to see if I can make the code execution faster than 1.200 sec with it, instead of using enumerate()
    curr_num_no_changes = curr_num


    while True:
        if curr_position % 2 == 0:
            curr_even_sum += curr_num % 10
            curr_num = floor(curr_num / 10)
        else:
            curr_odd_sum += curr_num % 10
            curr_num = floor(curr_num / 10)
        curr_position += 1
        if curr_num == 0:
            break
        """
        Alternatively:
        
        for curr_num in range(range_min_num, range_max_num + 1):
            num_to_str = str(curr_num)
            for index, digit in enumerate(num_to_str):
                if index % 2 == 0:
                    curr_even_sum += int(digit)
                else:
                    curr_odd_sum += int(digit)
        """

    curr_num = curr_num_no_changes

    if curr_odd_sum == curr_even_sum:
        print(curr_num, end= " ")

    curr_odd_sum = 0
    curr_even_sum = 0
    curr_position = 0