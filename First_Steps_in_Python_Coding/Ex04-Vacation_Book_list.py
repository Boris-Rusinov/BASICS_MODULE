book_pages = int(input())
pages_read_per_hour = int(input())
deadline = int(input())

hours_to_read_book = book_pages / pages_read_per_hour

pages_to_read_per_day = hours_to_read_book / deadline

print(pages_to_read_per_day)