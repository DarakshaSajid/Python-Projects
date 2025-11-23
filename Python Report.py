import datetime
# ---------------- DATA STORAGE & ID GENERATOR (Minor Module) ---------------- #
books = [#Name of the books 
    {"id": 1, "title": "Python Programming", "author": "Mark Lutz", "total": 5, "available": 5},
    {"id": 2, "title": "Data Science from Scratch", "author": "Joel Grus", "total": 4, "available": 4},
    {"id": 3, "title": "Artificial Intelligence: A Modern Approach", "author": "Stuart Russell", "total": 3, "available": 3},
    {"id": 4, "title": "Machine Learning", "author": "Tom Mitchell", "total": 4, "available": 4},
    {"id": 5, "title": "Clean Code", "author": "Robert C. Martin", "total": 6, "available": 6},
    {"id": 6, "title": "Operating System Concepts", "author": "Silberschatz", "total": 5, "available": 5},
    {"id": 7, "title": "Database System Concepts", "author": "Henry Korth", "total": 4, "available": 4},
    {"id": 8, "title": "Introduction to Algorithms", "author": "Cormen", "total": 3, "available": 3},
    {"id": 9, "title": "Computer Networks", "author": "Andrew S. Tanenbaum", "total": 6, "available": 6},
    {"id": 10, "title": "Let Us C", "author": "Yashwant Kanetkar", "total": 8, "available": 8},
]

users = []  #array for user input
issued_books = []  #array for book issued 
book_id = 11  #No.of books in the list
user_id = 1
fine = 10     # The fine per day after the due date 
daysborrowed = 7    # Allowed period
# ---------------- BOOK MANAGEMENT MODULE ---------------- #
def add_book(title, author, total_copies):#defining function for books if some book is to be added
    global book_id
    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "total": total_copies,
        "available": total_copies
    })
    print(f"Book Added Successfully! ID: {book_id}")# Printing that the book is added
    book_id += 1

def view_books():#To view the book list
    print("\n--- BOOK LIST ---")
    for b in books:
        print(f"ID:{b['id']} | {b['title']} by {b['author']} | Total:{b['total']} | Available:{b['available']}")

def search_book(book_id):# To search for a book using the book ID
    for b in books:
        if b["id"] == book_id:
            return b
    return None
# ---------------- USER MANAGEMENT MODULE ---------------- #

def add_user(name):#Defining a function to add name of the users
    global user_id
    users.append({"id": user_id, "name": name})
    print(f"User Added Successfully! ID: {user_id}")
    user_id += 1

def view_users():#For printing the list of users 
    print("\n--- USER LIST ---")
    for u in users:
        print(f"ID:{u['id']} | Name: {u['name']}")

def search_user(uid):#To search for a user using the User ID
    for user in users:
        if user["id"] == uid:
            return user
    return None
# ---------------- BOOK ALLOCATION AND RETURN+ FINEMODULE ---------------- #
def issue_book(uid, bid):#Function for searching a book and it's availability 
    user = search_user(uid)#To search for the user
    book = search_book(bid)# To search for the book

    if user and book:
        if book["available"] > 0:
            due_date = datetime.datetime.now() + datetime.timedelta(days=BORROW_DAYS)
            issued_books.append({"user_id": uid, "book_id": bid, "due": due_date})
            book["available"] -= 1
            print(f"Book '{book['title']}' issued to {user['name']} successfully.")
            print(f"Due Date: {due_date.strftime('%Y-%m-%d')}")
        else:
            print("No copies available.")#Printing if the total no.of books available for a single book-type has been issued 
    else:
        print("User or Book not found.")#Printing if user or book is not found
def return_book(uid, bid):#To show the date and time of the book to be returned after it has been issued 
    for record in issued_books:#To record the book id 
        if record["user_id"] == uid and record["book_id"] == bid:
            issued_books.remove(record)#to remove the books issued
            book = search_book(bid)
            book["available"] += 1

            today = datetime.datetime.now()#To record the date and time 
            overdue_days = (today - record["due"]).days

            if overdue_days > 0:#To record the no.of days the book was returned late and calculate fine accordingly
                fine = overdue_days * FINE_RATE
                print(f"Book returned late by {overdue_days} days. Fine = ₹{fine}")#To print the no.of days it was retuned late and fine
            else:
                print("Book returned on time. No fine.")#To print if the book was returned on time
            return

    print("No record found for return.")
    def view_issued_books():#To view the list of issued book
    print("\n--- ISSUED BOOKS LIST ---")
    if not issued_books:
        print("No books issued.")#To print if no book is issued 
        return

    for r in issued_books:
        user = search_user(r["user_id"])
        book = search_book(r["book_id"])
        #To print the book issued, name of the user and also the due date
        print(f"{book['title']} -> {user['name']} | Due Date: {r['due'].strftime('%Y-%m-%d')}")
        def menu():#To print all the content
    while True:
        print("\n===== LIBRARY BOOK ALLOCATION SYSTEM =====")
        print("1. Add Book")
        print("2. Add User")
        print("3. View Books")
        print("4. View Users")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. View Issued Books")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":#To add information of a add new book
            add_book(input("Enter Title: "), input("Enter Author: "), int(input("Enter Total Copies: ")))
        elif choice == "2":# To add information of a new user
            add_user(input("Enter User Name: "))
        elif choice == "3":#To view the list of books available
            view_books()
        elif choice == "4":#To view the list of users
            view_users()
        elif choice == "5":#To issue a book
            issue_book(int(input("Enter User ID: ")), int(input("Enter Book ID: ")))
        elif choice == "6":#To return a book
            return_book(int(input("Enter User ID: ")), int(input("Enter Book ID: ")))
        elif choice == "7":#To view the list of issued books
            view_issued_books()
        elif choice == "8":#To make an exit from the system 
            print("Thank you for using the Library System!")
            break
        else:
            print("Invalid option! Try again.")

menu()
