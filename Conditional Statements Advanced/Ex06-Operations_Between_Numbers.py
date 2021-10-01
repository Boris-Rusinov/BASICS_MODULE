N1 = int(input())
N2 = int(input())
operation_type = input()

result = 0.00

if N2 > 0 or N2 < 0:
    if operation_type == "+":
        result = N1 + N2
        if result % 2 == 0:
            print(f"{N1} {operation_type} {N2} = {result} - even")
        else:
            print(f"{N1} {operation_type} {N2} = {result} - odd")
    elif operation_type == "-":
        result = N1 - N2
        if result % 2 == 0:
            print(f"{N1} {operation_type} {N2} = {result} - even")
        else:
            print(f"{N1} {operation_type} {N2} = {result} - odd")
    elif operation_type == "*":
        result = N1 * N2
        if result % 2 == 0:
            print(f"{N1} {operation_type} {N2} = {result} - even")
        else:
            print(f"{N1} {operation_type} {N2} = {result} - odd")
    elif operation_type == "/":
        result = N1 / N2
        print(f"{N1} {operation_type} {N2} = {result:.2f}")
    elif operation_type == "%":
        result = N1 % N2
        print(f"{N1} {operation_type} {N2} = {result}")
else:
    print(f"Cannot divide {N1} by zero")