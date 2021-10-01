import sys

num_amount = int(input())

even_min_num = sys.maxsize
even_max_num = -sys.maxsize
odd_min_num = sys.maxsize
odd_max_num = -sys.maxsize

even_sum = 0
odd_sum = 0

amount_even_num = 0
amount_odd_num = 0

for curr_index in range(1, num_amount + 1):
    curr_num = float(input())
    if curr_index % 2 == 0:
        even_sum += curr_num
        amount_even_num += 1
        if curr_num > even_max_num:
            even_max_num = curr_num
        if curr_num < even_min_num:
            even_min_num = curr_num
    else:
        odd_sum += curr_num
        amount_odd_num += 1
        if curr_num > odd_max_num:
            odd_max_num = curr_num
        if curr_num < odd_min_num:
            odd_min_num = curr_num

print(f"OddSum={odd_sum:.2f},")
if amount_odd_num == 0:
    print(f"OddMin=No,")
    print(f"OddMax=No,")
else:
    print(f"OddMin={odd_min_num:.2f},")
    print(f"OddMax={odd_max_num:.2f},")

print(f"EvenSum={even_sum:.2f},")
if amount_even_num == 0:
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
else:
    print(f"EvenMin={even_min_num:.2f},")
    print(f"EvenMax={even_max_num:.2f}")