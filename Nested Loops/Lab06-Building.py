building_floor_count = int(input())
floor_room_count = int(input())

for curr_col_index in reversed(range(1, building_floor_count + 1)):
    for curr_row_index in range(0, floor_room_count):

        if curr_col_index == building_floor_count:
            print(f"L{curr_col_index}{curr_row_index}", end=" ")

        if curr_col_index % 2 == 0 and curr_col_index != building_floor_count:
            print(f"O{curr_col_index}{curr_row_index}", end=" ")
        elif curr_col_index % 2 == 1 and curr_col_index != building_floor_count:
            print(f"A{curr_col_index}{curr_row_index}", end=" ")
    print("")