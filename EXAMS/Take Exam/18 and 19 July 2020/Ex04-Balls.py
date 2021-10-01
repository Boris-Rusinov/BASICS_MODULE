ball_count = int(input())

curr_color = ""
red_ball_color_count = 0
orange_ball_color_count = 0
yellow_ball_color_count = 0
white_ball_color_count = 0
other_ball_colors_count = 0
divides_from_black_balls_count = 0
total_points = 0

for curr_index in range(0, ball_count):
    curr_ball_color = input()

    if curr_ball_color == "red":
        red_ball_color_count += 1
        total_points += 5
    elif curr_ball_color == "orange":
        orange_ball_color_count += 1
        total_points += 10
    elif curr_ball_color == "yellow":
        yellow_ball_color_count += 1
        total_points += 15
    elif curr_ball_color == "white":
        white_ball_color_count += 1
        total_points += 20
    elif curr_ball_color == "black":
        divides_from_black_balls_count += 1
        total_points /= 2
    else:
        other_ball_colors_count += 1

print(f"Total points: {int(total_points)}")
print(f"Points from red balls: {red_ball_color_count}")
print(f"Points from orange balls: {orange_ball_color_count}")
print(f"Points from yellow balls: {yellow_ball_color_count}")
print(f"Points from white balls: {white_ball_color_count}")
print(f"Other colors picked: {other_ball_colors_count}")
print(f"Divides from black balls: {divides_from_black_balls_count}")