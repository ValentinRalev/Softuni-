book = input()
book_name = input()
tries = 0

while book_name != book:
    if book_name == "No More Books":
        break

    tries += 1
    book_name = input()


if book_name == book:
    print(f"You checked {tries} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {tries} books.")

