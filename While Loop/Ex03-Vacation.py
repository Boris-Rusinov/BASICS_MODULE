vacation_cost = float(input())
starting_funds = float(input())

total_saved_funds = starting_funds
amount_spending_days = 0
days_taken_to_save_needed_money = 0

if total_saved_funds >= vacation_cost:
    print(f"You saved the money for {days_taken_to_save_needed_money} days.")
else:
    action = input()
    curr_money = float(input())
    while True:
        if action == "save":
            total_saved_funds += curr_money
            days_taken_to_save_needed_money += 1
            amount_spending_days = 0
            if total_saved_funds >= vacation_cost:
                print(f"You saved the money for {days_taken_to_save_needed_money} days.")
                break
        elif action == "spend":
            total_saved_funds -= curr_money
            amount_spending_days += 1
            days_taken_to_save_needed_money += 1
            if total_saved_funds < 0:
                total_saved_funds = 0
            if amount_spending_days == 5:
                print("You can't save the money.")
                print(f"{days_taken_to_save_needed_money}")
                break

        action = input()
        curr_money = float(input())