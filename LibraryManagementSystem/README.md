# Library Management System

A simple Python program that manages a small list of books. It runs in the
terminal and lets you add, search, issue, return, delete, and display books
using a menu.

## Overview

This project is a beginner-friendly library system. All books are stored in
a list while the program is running, and you interact with it by typing
numbers from a menu.

## Features

- Display all books with their status (Available / Issued)
- Add a new book (ID, name, author)
- Search for a book by name
- Issue a book (mark it as issued)
- Return a book (mark it as available again)
- Delete a book from the list

## Technologies / Tools Used

- Python 3 (no extra libraries needed — just the standard `input()` and `print()`)

## Steps to Install & Run

1. Make sure Python 3 is installed on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:
   ```bash
   python main.py
   ```
5. Use the on-screen menu (type a number 1-7 and press Enter) to use the program.

## Instructions for Testing

There is no separate test file — test the program manually by running it and
trying each menu option:

1. Choose option 1 to see the starting list of books.
2. Choose option 2 to add a new book, then option 1 again to confirm it appears.
3. Choose option 3 and type part of a book name to check that search works.
4. Choose option 4 to issue a book, then option 1 to see its status change to "Issued".
5. Choose option 5 to return the same book and confirm its status goes back to "Available".
6. Choose option 6 to delete a book, then option 1 to confirm it is gone.
7. Choose option 7 to exit the program.

## Note

Books are only kept in memory — once you close the program, any changes
(added or deleted books) are lost and it restarts with the original 3 books
the next time you run it.
