command = input()

curr_steps = 0

steps_goal = 10000

while True:
    if command == "Going home":
        curr_steps = int(input())
        steps_goal -= curr_steps
        if steps_goal > 0:
            print(f"{steps_goal} more steps to reach goal.")
        else:
            print("Goal reached! Good job!")
            print(f"{abs(steps_goal)} steps over the goal!")
        break

    curr_steps = int(command)
    steps_goal -= curr_steps
    if steps_goal <= 0:
        print("Goal reached! Good job!")
        print(f"{abs(steps_goal)} steps over the goal!")
        break
    command = input()