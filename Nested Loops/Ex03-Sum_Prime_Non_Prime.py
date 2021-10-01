prime_nums_sum = 0
non_prime_nums_sum = 0
curr_num = 0
no_remainder_divisions = 0

while True:
    command = input()
    no_remainder_divisions = 0

    if command == "stop":
        break
    else:
        curr_num = int(command)

        if curr_num == 0:
            continue
        elif curr_num == 1:
            non_prime_nums_sum += curr_num
        elif curr_num < 0:
            print("Number is negative.")
        else:
            for curr_divisor in range(1, curr_num + 1):
                if curr_num % curr_divisor == 0:
                    no_remainder_divisions += 1

            if no_remainder_divisions == 2:
                prime_nums_sum += curr_num
            else:
                non_prime_nums_sum += curr_num

print(f"Sum of all prime numbers is: {prime_nums_sum}")
print(f"Sum of all non prime numbers is: {non_prime_nums_sum}")