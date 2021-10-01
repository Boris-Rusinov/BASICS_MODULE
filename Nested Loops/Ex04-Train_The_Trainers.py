judge_count = int(input())

curr_presentation_avg_grade = 0.00
all_presentations_avg_grade = 0.00
all_presentations_count = 0
curr_presentation_name = 0
curr_presentation_grade = 0

while True:
    curr_presentation_name = input()

    if curr_presentation_name == "Finish":
        all_presentations_avg_grade /= all_presentations_count
        print(f"Student's final assessment is {all_presentations_avg_grade:.2f}.")
        break
    else:
        for curr_judge in range(0, judge_count):
            curr_presentation_grade = float(input())
            curr_presentation_avg_grade += curr_presentation_grade

        curr_presentation_avg_grade /= judge_count
        print(f"{curr_presentation_name} - {curr_presentation_avg_grade:.2f}.")
        all_presentations_avg_grade += curr_presentation_avg_grade
        curr_presentation_avg_grade = 0
        all_presentations_count += 1