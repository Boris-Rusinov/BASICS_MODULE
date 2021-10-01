import sys

command = input()

largest_num = -sys.maxsize
curr_num = 0

while command != "Stop":
    curr_num = int(command)
    if curr_num > largest_num:
        largest_num = curr_num

    command = input()

print(largest_num)