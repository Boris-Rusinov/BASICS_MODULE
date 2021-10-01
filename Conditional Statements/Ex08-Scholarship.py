from math import floor

income = float(input())
avg_grade = float(input())
min_work_salary = float(input())

social_scholarship = 0.00
excellent_results_scholarship = 0.00

if income < min_work_salary and avg_grade > 4.5:
    social_scholarship = min_work_salary * 0.35

if avg_grade >= 5.5:
    excellent_results_scholarship = 25 * avg_grade

if social_scholarship == 0 and excellent_results_scholarship == 0 :
    print("You cannot get a scholarship!")
elif(social_scholarship != 0 and excellent_results_scholarship == 0):
    print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
elif(social_scholarship == 0 and excellent_results_scholarship != 0):
    print(f"You get a scholarship for excellent results {floor(excellent_results_scholarship)} BGN")
else:
    if(social_scholarship < excellent_results_scholarship):
        print(f"You get a scholarship for excellent results {floor(excellent_results_scholarship)} BGN")
    elif(social_scholarship > excellent_results_scholarship):
        print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
    elif (social_scholarship == excellent_results_scholarship):
        print(f"You get a scholarship for excellent results {floor(excellent_results_scholarship)} BGN")

