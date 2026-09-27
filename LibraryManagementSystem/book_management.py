def add_book(books):
    print("\n--- ADD BOOK ---")
    book_id = int(input("Enter Book ID: "))
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    books.append({
        "id": book_id,
        "name": name,
        "author": author,
        "issued": False
    })

    print("Book added successfully.")


def delete_book(books):
    print("\n--- DELETE BOOK ---")
    book_id = int(input("Enter Book ID: "))

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            print("Book deleted successfully.")
            return

    print("Book not found.")
