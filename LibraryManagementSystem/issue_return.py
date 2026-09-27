def issue_book(books):
    print("\n--- ISSUE BOOK ---")
    book_id = int(input("Enter Book ID: "))

    for book in books:
        if book["id"] == book_id:
            if book["issued"]:
                print("Book is already issued.")
            else:
                book["issued"] = True
                print("Book issued successfully.")
            return

    print("Book not found.")


def return_book(books):
    print("\n--- RETURN BOOK ---")
    book_id = int(input("Enter Book ID: "))

    for book in books:
        if book["id"] == book_id:
            if book["issued"]:
                book["issued"] = False
                print("Book returned successfully.")
            else:
                print("Book was not issued.")
            return

    print("Book not found.")
