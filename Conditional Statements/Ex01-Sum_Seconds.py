from math import floor

first_runner_secs = int(input())
second_runner_secs = int(input())
third_runner_secs = int(input())

#Faster and easier way to do this
total_secs = first_runner_secs + second_runner_secs + third_runner_secs

mins = floor(total_secs / 60)
secs = total_secs % 60

if(secs >= 0 and secs <= 9):
    print(f"{mins}:0{secs}")
else:
    print(f"{mins}:{secs}")





#More time consuming and roundabout way to solve this
"""

if(first_runner_secs + second_runner_secs >= 60):
    mins += 1
    secs += (first_runner_secs + second_runner_secs - 60)
else:
    secs += (first_runner_secs + second_runner_secs)

if(secs + third_runner_secs >= 60):
    mins += 1
    secs = secs + third_runner_secs - 60
else:
    secs += third_runner_secs

if(secs >= 0 and secs <= 9):
    print(f"{mins}:0{secs}")
else:
    print(f"{mins}:{secs}")
"""