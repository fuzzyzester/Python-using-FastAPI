from dotenv import load_dotenv
from typing import List
import os
import requests
from schemas import Item

load_dotenv()

DB_URL = os.getenv("DB_URL") # "http://localhost:8000"


def url(route: str):
    return f"{DB_URL}{route}"


print("Welcome to Rianna's Book Corner")


def print_menu():
    print(
        """
    1: Add book
    2: Get list of books
    3: Delete book
    4: Update book
    5: Exit program
    """
    )


def add_book():
    print("Add a book")
    title = input("Book title: ")
    author = input("Book author: ")
    new_book = Item(title=title, author=author)
    res = requests.post(url("/add-book"), json=new_book.dict())
    print(res.json())


def get_books():
    print("Get the book list")
    res = requests.get(url("/list-books"))
    data = res.json()
    books = data.get('books')
    if not books:
        print('No books found')
        return
    for book in books:
        print("_________")
        print(f"ID: {book.id}")
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")


def delete_book():
    print("Delete a book")
    book_id = input("ID of the book you wish to delete: ")
    if not str.isdigit(book_id):
        print("IDs are integers")
        return
    res = requests.delete(url(f"/delete-book/{book_id}"))
    print(res.json())


def update_book():
    print("Update book")
    book_id = input("ID of book you wish to update: ")
    if not str.isdigit(book_id):
        print("IDs are integers")
        return

    res = requests.get(url(f"/book-by-index/{book_id}"))
    data = res.json()
    book = data.get('title')
    author = data.get('author')

    title = input(f"Current book title: {book}, enter new title (leave blank if same): ")
    author = input(f"Current book author: {author}, enter new author (leave blank if same): ")

    if not title:
        title = book
    if not author:
        author = data.get('author')

    updated_book = Item(title=title, author=author)
    res = requests.put(url(f"/update-book/{book_id}"), json=updated_book.dict())
    print(res.json())


def main():
    print_menu()
    choice = input("What do you like to do? Please enter the number of your choice. ")
    choice = choice.strip()
    if not str.isdigit(choice):
        print("Please enter a valid option")
        return

    match int(choice):
        case 1:
            add_book()
        case 2:
            get_books()
        case 3:
            delete_book()
        case 4:
            update_book()
        case 5:
            exit()
        case _:
            print("Please enter a valid option")

while __name__ == "__main__":
    main()
