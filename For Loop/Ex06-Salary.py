tab_amount = int(input())
salary = int(input())

for curr_index in range(0, tab_amount):
    curr_website = input()

    if curr_website == "Facebook":
        salary -= 150
    elif curr_website == "Instagram":
        salary -= 100
    elif curr_website == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break


if salary != 0:
    print(salary)