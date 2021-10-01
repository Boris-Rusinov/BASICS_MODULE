command = input()

money_to_add = 0.00
bank_account = 0.00

while True:
    if command == "NoMoreMoney":
        print(f"Total: {bank_account:.2f}")
        break
    else:
        money_to_add = float(command)
        if money_to_add < 0:
            print("Invalid operation!")
            print(f"Total: {bank_account:.2f}")
            break
        else:
            bank_account += money_to_add
            print(f"Increase: {money_to_add:.2f}")
    command = input()