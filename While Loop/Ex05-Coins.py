change_to_give = float(input())

coin_count = 0

while True:
    if change_to_give >= 2:
        change_to_give -= 2
        change_to_give = round(change_to_give, 2)
        coin_count += 1
    elif change_to_give >= 1:
        change_to_give -= 1
        change_to_give = round(change_to_give, 2)
        coin_count += 1
    elif change_to_give >= 0.50:
        change_to_give -= 0.50
        change_to_give = round(change_to_give, 2)
        coin_count += 1
    elif change_to_give >= 0.20:
        change_to_give -= 0.20
        change_to_give = round(change_to_give, 2) #Will get shit like 0.089999997 unless round() is used
        coin_count += 1
    elif change_to_give >= 0.10:
        change_to_give -= 0.10
        change_to_give = round(change_to_give, 2)
        coin_count += 1
    elif change_to_give >= 0.05:
        change_to_give -= 0.05
        change_to_give = round(change_to_give, 2)
        coin_count += 1
    elif change_to_give >= 0.02:
        change_to_give -= 0.02
        change_to_give = round(change_to_give, 2)
        coin_count += 1
    elif change_to_give >= 0.01:
        change_to_give -= 0.01
        change_to_give = round(change_to_give, 2)
        coin_count += 1

    if change_to_give == 0:
        print(coin_count)
        break