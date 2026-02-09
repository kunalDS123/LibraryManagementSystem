import tkinter as tk
from tkinter import messagebox
from library import Library, BooknotAvailbleError

lib = Library()

root = tk.Tk() # cretes the main application window
root.title("Smart Library Management System") #Window Title
root.geometry("500x400")

#--------------Heading-----------
tk.Label(   #lable - Used to display text
    root,      #Parent Window
    text="Smart Library Management System",
    font=("Arial" , 18, "bold") #Font Style
).pack(pady=10) #.pack() - layout manager(auto placement)



#-------add_Book-----------
def open_add_book():
    win = tk.Toplevel(root)
    win.title("Add Book")

    tk.Label(win, text="Title").grid(row=0, column=0)
    tk.Label(win, text="Author").grid(row=1, column=0)
    tk.Label(win, text="Copies").grid(row=2, column=0)

    title = tk.Entry(win)
    author = tk.Entry(win)
    copies = tk.Entry(win)

    title.grid(row=0, column=1)
    author.grid(row=1, column=1)
    copies.grid(row=2, column=1)

    def submit():
        try:
            msg = lib.add_book(
                title.get(),
                author.get(),
                int(copies.get())
            )
            messagebox.showinfo("Success", msg)
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Book", command=submit).grid(row=3,columnspan=2)


#------------Register User Window------------------

def open_register_user():
    win =tk.Toplevel(root)
    win.title("Rigester User")

    tk.Label(win, text="Name").grid(row=0,column=0)
    tk.Label(win,text="Grade").grid(row=1, column=0)

    name = tk.Entry(win)
    grade = tk.Entry(win)

    name.grid(row=0,column=1)
    grade.grid(row=1,column=1)

    def submit():
        try:
            msg = lib.register_user(name.get(), grade.get())
            messagebox.showinfo("Success", msg)
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    tk.Button(win, text="Regester", command=submit).grid(row=2, columnspan=2)



#---------------Issue Book Window-------------------
def open_issue_book():
    win = tk.Toplevel(root)
    win.title("Issue Book")

    tk.Label(win,text="Book ID").grid(row=0,column=0)
    tk.Label(win, text="User ID").grid(row=1, column=0)

    book_id = tk.Entry(win)
    user_id = tk.Entry(win)

    book_id.grid(row=0,column=1)
    user_id.grid(row=1, column=1)

    def submit():
        try:
            msg = lib.issue_book(book_id.get(), user_id.get())
            messagebox.showinfo("Sucess", msg)
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", e)

    tk.Button(win, text="Issue Book", command=submit).grid(row=2,columnspan=2)


#-------------Return Book Window------------------
def open_return_book():
    win = tk.Toplevel()
    win.title("Retun Book")

    tk.Label(win, text="Book ID").grid(row=0,column=0)
    tk.Label(win, text="User ID").grid(row=1, column=0)

    book_id = tk.Entry(win)
    user_id = tk.Entry(win)

    book_id.grid(row=0,column=1)
    user_id.grid(row=1,column=1)

    def submit():
        try:
            msg= lib.return_book(book_id.get(), user_id.get())
            messagebox.showinfo("Info", msg)
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    tk.Button(win, text="Return", command=submit).grid(row=3,columnspan=2)

#-------View Books--------

def view_books():
    win= tk.Toplevel(root)
    win.title("Books")

    if not lib.books:
        tk.Label(win, text="No books available!!").pack()
        return
    
    for book in lib.books.values():
        tk.Label(win, text= str(book)).pack()

#------View Users----------
def view_users():
    win = tk.Toplevel(root)
    win.title("Users")

    if not lib.users:
        tk.Label(win, text="No user registerd").pack()
        return
    for user in lib.users.values():
        tk.Label(win,text=str(user)).pack()





tk.Button(root, text="Add Book", width=25, command=open_add_book).pack(pady=4)
tk.Button(root, text="Rigester User", width=25, command=open_register_user).pack(pady=4)
tk.Button(root, text="Issue Book", width=25, command=open_issue_book).pack(pady=4)
tk.Button(root, text="Return Book", width=25, command=open_return_book).pack(pady=4)
tk.Button(root, text="View Book", width=25, command=view_books).pack(pady=4)
tk.Button(root, text="View Users", width=25, command=view_users).pack(pady=4)


root.mainloop()

