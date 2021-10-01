from sys import maxsize

person_name = input()

# a-z ==> 97-122; A-Z ==> 65-90
# From char to ascii ==> ord("a") => 97
# 10 points for correct char-ascii guess, 2 points otherwise

name_length = len(person_name)
largest_total_points = -maxsize
curr_total_points = 0
curr_num_to_check = 0
curr_winner = ""

while person_name != "Stop":
    for curr_guess_index in range(0, name_length):
        curr_num_to_check = int(input())

        if ord(person_name[curr_guess_index]) == curr_num_to_check:
            curr_total_points += 10
        else:
            curr_total_points += 2

    if curr_total_points > largest_total_points:
        largest_total_points = curr_total_points
        curr_winner = person_name
    elif curr_total_points == largest_total_points:
        curr_winner = person_name

    person_name = input()
    name_length = len(person_name)
    curr_total_points = 0

print(f"The winner is {curr_winner} with {largest_total_points} points!")