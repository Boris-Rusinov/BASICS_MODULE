needed_book = input()

curr_book = input()

book_count = 0

while True:
    if curr_book == needed_book:
        print(f"You checked {book_count} books and found it.")
        break

    if curr_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {book_count} books.")
        break

    book_count += 1

    curr_book = input()

