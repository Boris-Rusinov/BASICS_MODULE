free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())

free_space_vol = free_space_width * free_space_length * free_space_height

command = input()

curr_box_vol = 0

while True:
    if command == "Done":
        print(f"{free_space_vol} Cubic meters left.")
        break

    curr_box_vol = int(command)
    free_space_vol -= curr_box_vol

    if free_space_vol < 0:
        print(f"No more free space! You need {abs(free_space_vol)} Cubic meters more.")
        break

    command = input()
