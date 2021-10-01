num = float(input())
entry_unit = input()
exit_unit = input()

if(entry_unit == "mm" and exit_unit == "cm"):
    num /= 10
elif(entry_unit == "mm" and exit_unit == "m"):
    num /= 1000
elif (entry_unit == "cm" and exit_unit == "mm"):
    num *= 10
elif (entry_unit == "cm" and exit_unit == "m"):
    num /= 100
elif (entry_unit == "m" and exit_unit == "cm"):
    num *= 100
elif (entry_unit == "m" and exit_unit == "mm"):
    num *= 1000

print(f"{num:.3f}")