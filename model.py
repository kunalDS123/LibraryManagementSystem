class book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = int(copies)
    
    def __str__(self):
        return(f"Book Id = {self.book_id} | Books Title = {self.title} | author = {self.author} | No of books = {self.copies}")
    

class person:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

class student(person):
    def __init__(self, name, user_id, grade):
        super().__init__(name, user_id)
        self.grade = grade

    def __str__(self):
        return(f"Name = {self.name} | User Id = {self.user_id} | Grade = {self.grade}")


    