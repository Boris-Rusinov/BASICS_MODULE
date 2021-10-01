allowed_unsatisfactory_grades = int(input())

avg_grade = 0.00
exercise_count = 0
curr_ex_name = ""                  #Name of current exercise
curr_ex_grade = 0                  #Grade of current exercise
unsatisfactory_grades_count = 0

command = input()

while command != "Enough":
    curr_ex_name = command
    curr_ex_grade = int(input())

    if curr_ex_grade <= 4:
        unsatisfactory_grades_count += 1

    if unsatisfactory_grades_count == allowed_unsatisfactory_grades:
        print(f"You need a break, {unsatisfactory_grades_count} poor grades.")
        break

    avg_grade += curr_ex_grade
    exercise_count += 1

    command = input()

if unsatisfactory_grades_count != allowed_unsatisfactory_grades:
    avg_grade /= exercise_count
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {exercise_count}")
    print(f"Last problem: {curr_ex_name}")