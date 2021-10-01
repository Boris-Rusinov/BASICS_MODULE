power = int(input())

current_result = 0

for current_pwr in range(0, power + 1, 2):
    current_result = pow(2, current_pwr)
    print(current_result)