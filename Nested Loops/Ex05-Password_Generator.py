n = int(input())
l = int(input())

curr_symbol_4_letter = ""
curr_symbol_5_letter = ""

curr_largest_num = 0

for curr_symbol_1 in range(1, n):
    for curr_symbol_2 in range(1, n):

        if curr_symbol_1 >= curr_symbol_2:
            curr_largest_num = curr_symbol_1
        else:
            curr_largest_num = curr_symbol_2

        for curr_symbol_3 in range(0, l):
            for curr_symbol_4 in range(0, l):
                for curr_symbol_5 in range(curr_largest_num + 1, n + 1):
                    curr_symbol_3_letter = chr(97 + curr_symbol_3)
                    curr_symbol_4_letter = chr(97 + curr_symbol_4)

                    print(f"{curr_symbol_1}{curr_symbol_2}{curr_symbol_3_letter}{curr_symbol_4_letter}{curr_symbol_5}", end=" ")