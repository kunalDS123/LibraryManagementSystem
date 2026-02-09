from model import book, student
from utils import log_action,generate_id
from datetime import datetime


class BooknotAvailbleError(Exception):
    pass

class Library:
    fine_per_day = 5

    def __init__(self):
        self.books = {}
        self.users = {}
        self.transaction = []
    
    @log_action
    # def add_book(self):
    #     book_id = generate_id("B", len(self.books)+1)
    #     title = input("Enter book title : ")
    #     author = input("Enter Author : ")
    #     copies = input("Enter number of copies : ")

    #     self.books[book_id] = book(book_id, title, author, copies)
    #     print("Book added successfully")
    
    def add_book(self,title, author, copies):
        book_id = generate_id("B",len(self.books)+1)
        self.books[book_id] = book(book_id, title, author, copies)
        return "Book added successfully!!"
    
    @log_action
    # def register_user(self):
    #     user_id = generate_id("U",len(self.users)+1)
    #     name = input("Enter student name: ")
    #     grade = input("Enter grade: ")

    #     self.users[user_id] = student(name, user_id, grade)
    #     print ("user regesterd successfully!!")
    def register_user(self, name, grade):
        user_id = generate_id("U" , len(self.users)+1)
        self.users[user_id] = student( name, user_id, grade)
        return "User registered Successfully!!"   

    @log_action
    def issue_book(self, book_id, user_id):
        #check if book exist
        if book_id not in self.books:
            raise BooknotAvailbleError("Book Id does not exist")
        
        #check if user exist
        if user_id not in self.users:
            raise BooknotAvailbleError("User ID does not exist")
        
        #check if copies are available
        if self.books[book_id].copies <= 0:
            raise BooknotAvailbleError("No copies available for this book")
        
        #Issue Book
        self.books[book_id].copies -=1
        issue_date = datetime.now().strftime("%Y-%m-%d")
        self.transaction.append((book_id, user_id, issue_date))
        return "Book Issued Successfully!!"

    @log_action    
    def return_book(self,book_id, user_id):
        for record in self.transaction:
            if record[0] == book_id and record[1] == user_id:
                issue_date = datetime.strptime(record[2], "%Y-%m-%d")
                return_date = datetime.now()

                days = (return_date - issue_date).days
                fine = (days - 7) * Library.fine_per_day if days > 7 else 0

                self.books[book_id].copies += 1 
                return  f"Book returned! Fine: Rs{fine}"
            
        return "Transaction not found."
    
    @log_action
    def view_books(self):
        if not self.books:
            print("No books Found!!")
            return
        
        available = [book for book in self.books.values() if book.copies > 0]
        for book in available:
            print(book)
        

    @log_action
    def view_users(self):
        if not self.users:
            print("No user is regesterd yet")
            return
        # user_available = [user in self.users.values()]
        for user in self.users.values():
            print(user)

    