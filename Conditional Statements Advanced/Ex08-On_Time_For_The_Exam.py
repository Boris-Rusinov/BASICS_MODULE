from math import floor

exam_hour = int(input())
exam_mins = int(input())
arrival_hour = int(input())
arrival_mins = int(input())

exam_total_mins = exam_hour * 60 + exam_mins
arrival_total_mins = arrival_hour * 60 + arrival_mins

exam_and_arrival_diff = abs(exam_total_mins - arrival_total_mins)

current_late_hours = 0
current_late_mins = 0

current_early_hours = 0
current_early_mins = 0

if arrival_total_mins > exam_total_mins:
    print("Late")
    if exam_and_arrival_diff < 60:
        print(f"{exam_and_arrival_diff} minutes after the start")
    else:
        current_late_hours = floor(exam_and_arrival_diff / 60)
        current_late_mins = exam_and_arrival_diff % 60
        if current_late_mins <= 9:
            print(f"{current_late_hours}:0{current_late_mins} hours after the start")
        else:
            print(f"{current_late_hours}:{current_late_mins} hours after the start")
else:
    if exam_and_arrival_diff <= 30:
        print("On time")
        if exam_and_arrival_diff != 0:
            print(f"{exam_and_arrival_diff} minutes before the start")
    else:
        print("Early")
        if exam_and_arrival_diff < 60:
            print(f"{exam_and_arrival_diff} minutes before the start")
        else:
            current_early_hours = floor(exam_and_arrival_diff / 60)
            current_early_mins = exam_and_arrival_diff % 60
            if current_early_mins <= 9:
                print(f"{current_early_hours}:0{current_early_mins} hours before the start")
            else:
                print(f"{current_early_hours}:{current_early_mins} hours before the start")