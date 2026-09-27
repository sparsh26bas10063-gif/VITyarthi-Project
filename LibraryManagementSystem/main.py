from book_display import display_books, search_book
from book_management import add_book, delete_book
from issue_return import issue_book, return_book

books = [
    {"id": 1, "name": "how to solve it by computer", "author": "Dromey R G", "issued": False},
    {"id": 2, "name": "let us python", "author": "Yashavant Kanetkar", "issued": False},
    {"id": 3, "name": "Data Structures", "author": "Paul Deitel", "issued": False}
]

while True:
    print("\n==============================")
    print("   LIBRARY MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Display Books")
    print("2. Add Book")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_books(books)         
    elif choice == "2":
        add_book(books)               
    elif choice == "3":
        search_book(books)            
    elif choice == "4":
        issue_book(books)              
    elif choice == "5":
        return_book(books)            
    elif choice == "6":
        delete_book(books)             
    elif choice == "7":
        print("Thank you for using the Library System!")
        break
    else:
        print("Invalid choice. Please try again.")
