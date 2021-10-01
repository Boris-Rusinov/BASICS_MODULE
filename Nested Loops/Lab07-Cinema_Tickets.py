curr_film_name = input()

curr_film_total_seats = 0
curr_film_filled_seats = 0
curr_ticket = ""
curr_film_occupancy_percentage = 0.00

total_tickets = 0
total_student_tickets_percentage = 0.00
total_standard_tickets_percentage = 0.00
total_kid_tickets_percentage = 0.00

while curr_film_name != "Finish":
    curr_film_total_seats = int(input())

    while curr_film_total_seats > 0:
        curr_ticket = input()
        if curr_ticket == "student":
            total_student_tickets_percentage += 1
        elif curr_ticket == "standard":
            total_standard_tickets_percentage += 1
        elif curr_ticket == "kid":
            total_kid_tickets_percentage += 1

        if curr_ticket == "End":
            break
        curr_film_total_seats -= 1
        curr_film_filled_seats += 1
        total_tickets += 1

    curr_film_total_seats += curr_film_filled_seats
    curr_film_occupancy_percentage = curr_film_filled_seats / curr_film_total_seats * 100
    print(f"{curr_film_name} - {curr_film_occupancy_percentage:.2f}% full.")
    curr_film_filled_seats = 0

    curr_film_name = input()

total_student_tickets_percentage = total_student_tickets_percentage / total_tickets * 100
total_standard_tickets_percentage = total_standard_tickets_percentage / total_tickets * 100
total_kid_tickets_percentage = total_kid_tickets_percentage / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{total_student_tickets_percentage:.2f}% student tickets.")
print(f"{total_standard_tickets_percentage:.2f}% standard tickets.")
print(f"{total_kid_tickets_percentage:.2f}% kids tickets.")