football_team = input()
season_total_games = int(input())

if season_total_games < 1:
    print(f"{football_team} hasn't played any games during this season.")
else:
    season_total_points = 0
    total_wins = 0
    total_draws = 0
    total_losses = 0
    win_rate = 0.00

    curr_game_end_result = ""

    for curr_game in range(0, season_total_games):
        curr_game_end_result = input()

        if curr_game_end_result == "W":
            total_wins += 1
            season_total_points += 3
        elif curr_game_end_result == "D":
            total_draws += 1
            season_total_points += 1
        elif curr_game_end_result == "L":
            total_losses += 1

    win_rate = total_wins / season_total_games * 100

    print(f"{football_team} has won {season_total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {total_wins}")
    print(f"## D: {total_draws}")
    print(f"## L: {total_losses}")
    print(f"Win rate: {win_rate:.2f}%")