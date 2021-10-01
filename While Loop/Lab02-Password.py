username = input()
password = input()

while True:
    curr_password_attempt = input()

    if curr_password_attempt == password:
        print(f"Welcome {username}!")
        break