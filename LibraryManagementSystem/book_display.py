def display_books(books):
    print("\n--- BOOK LIST ---")
    if len(books) == 0:
        print("No books available.")
        return

    for book in books:
        status = "Issued" if book["issued"] else "Available"
        print("ID:", book["id"], "|", book["name"],
              "| Author:", book["author"], "|", status)


def search_book(books):
    print("\n--- SEARCH BOOK ---")
    name = input("Enter book name: ").lower()
    found = False

    for book in books:
        if name in book["name"].lower():
            print("ID:", book["id"])
            print("Name:", book["name"])
            print("Author:", book["author"])
            print("Status:", "Issued" if book["issued"] else "Available")
            found = True

    if not found:
        print("Book not found.")
