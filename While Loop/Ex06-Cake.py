width = int(input())
length = int(input())

curr_pieces_to_take = 0
total_pieces = width * length

while True:
    command = input()

    if command == "STOP":
        print(f"{total_pieces} pieces are left.")
        break
    else:
        curr_pieces_to_take = int(command)
        total_pieces -= curr_pieces_to_take
        if total_pieces <= 0:
            print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
            break
