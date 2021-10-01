student_name = input()
curr_year_avg_grade = float(input())
curr_year = 1
chances_to_do_year_again = 1
total_avg_grade = 0.00

while True:
    if curr_year_avg_grade < 4.00:
        chances_to_do_year_again -= 1
        if chances_to_do_year_again < 0:
            print(f"{student_name} has been excluded at {curr_year} grade")
            break
    else:
        total_avg_grade += curr_year_avg_grade

        if curr_year == 12:
            total_avg_grade /= 12
            print(f"{student_name} graduated. Average grade: {total_avg_grade:.2f}")
            break

        curr_year += 1

    curr_year_avg_grade = float(input())