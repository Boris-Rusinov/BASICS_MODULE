most_goals_of_best_player = 0
best_player = ""
is_there_hat_trick = False

while True:
    player_name = input()
    if player_name == "END":
        print(f"{best_player} is the best player!")
        if is_there_hat_trick:
            print(f"He has scored {most_goals_of_best_player} goals and made a hat-trick !!!")
        else:
            print(f"He has scored {most_goals_of_best_player} goals.")

        break

    all_curr_player_football_goals = int(input())
    if all_curr_player_football_goals > most_goals_of_best_player:
        most_goals_of_best_player = all_curr_player_football_goals
        best_player = player_name

    if all_curr_player_football_goals >= 3:
        is_there_hat_trick = True

    if all_curr_player_football_goals >= 10:
        print(f"{best_player} is the best player!")
        print(f"He has scored {most_goals_of_best_player} goals and made a hat-trick !!!")
        break