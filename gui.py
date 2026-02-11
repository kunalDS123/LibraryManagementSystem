import tkinter as tk
from tkinter import ttk, messagebox
from library import Library, BooknotAvailbleError

# ================= BACKEND =================
lib = Library()

# ================= ROOT =================
root = tk.Tk()
root.title("Smart Library Management System")
root.geometry("1100x650")
root.configure(bg="#f4f6f8")

# ================= STYLES =================
style = ttk.Style()
style.theme_use("clam")

style.configure("Header.TFrame", background="#2c3e50")
style.configure("Header.TLabel",
                background="#2c3e50",
                foreground="white",
                font=("Segoe UI", 16, "bold"))

style.configure("Action.TButton",
                font=("Segoe UI", 10, "bold"),
                padding=8)

style.configure("Section.TFrame",
                background="white",
                relief="raised")

style.configure("Section.TLabel",
                background="white",
                font=("Segoe UI", 12, "bold"))

# ================= HELPER FUNCTIONS =================
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"

def create_form_window(title, width=420, height=300):
    win = tk.Toplevel(root)
    win.title(title)
    win.configure(bg="#f4f6f8")
    win.resizable(False, False)

    x = root.winfo_x() + (root.winfo_width() // 2) - (width // 2)
    y = root.winfo_y() + (root.winfo_height() // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

    card = ttk.Frame(win, padding=20, style="Section.TFrame")
    card.pack(fill="both", expand=True, padx=15, pady=15)

    ttk.Label(card, text=title,
              font=("Segoe UI", 13, "bold")).pack(anchor="w", pady=(0, 15))

    return win, card

# ================= HEADER =================
header = ttk.Frame(root, style="Header.TFrame")
header.pack(fill="x")

ttk.Label(header,
          text="📚 Smart Library Management System",
          style="Header.TLabel").pack(side="left", padx=20, pady=15)

btn_frame = ttk.Frame(header, style="Header.TFrame")
btn_frame.pack(side="right", padx=20)

# ================= MAIN CONTENT =================
content = ttk.Frame(root)
content.pack(fill="both", expand=True, padx=20, pady=20)

left_panel = ttk.Frame(content, style="Section.TFrame")
left_panel.pack(side="left", fill="both", expand=True, padx=10)

right_panel = ttk.Frame(content, style="Section.TFrame")
right_panel.pack(side="right", fill="both", expand=True, padx=10)

# ================= BOOKS =================
ttk.Label(left_panel, text="📘 Newest 10 Books",
          style="Section.TLabel").pack(anchor="w", padx=15, pady=10)

books_listbox = tk.Listbox(left_panel, height=12,
                           font=("Segoe UI", 10),
                           bd=0, highlightthickness=0)
books_listbox.pack(fill="both", expand=True, padx=15)

# ================= USERS =================
ttk.Label(right_panel, text="👤 Newest 10 Users",
          style="Section.TLabel").pack(anchor="w", padx=15, pady=10)

users_listbox = tk.Listbox(right_panel, height=12,
                           font=("Segoe UI", 10),
                           bd=0, highlightthickness=0)
users_listbox.pack(fill="both", expand=True, padx=15)

# ================= REFRESH =================
def refresh_books_preview():
    books_listbox.delete(0, tk.END)
    for b in list(lib.books.values())[-10:]:
        books_listbox.insert(tk.END,
                             f"{b.book_id} | {b.title} | Available: {b.copies}")

def refresh_users_preview():
    users_listbox.delete(0, tk.END)
    for u in list(lib.users.values())[-10:]:
        users_listbox.insert(tk.END,
                             f"{u.user_id} | {u.name} | Grade: {u.grade}")

# ================= VIEW ALL =================
def view_all_books():
    win, card = create_form_window("All Books (Alphabetical)", 600, 400)
    lb = tk.Listbox(card, font=("Segoe UI", 10))
    lb.pack(fill="both", expand=True)
    for b in sorted(lib.books.values(), key=lambda x: x.title.lower()):
        lb.insert(tk.END, str(b))

def view_all_users():
    win, card = create_form_window("All Users (Alphabetical)", 600, 400)
    lb = tk.Listbox(card, font=("Segoe UI", 10))
    lb.pack(fill="both", expand=True)
    for u in sorted(lib.users.values(), key=lambda x: x.name.lower()):
        lb.insert(tk.END, str(u))

ttk.Button(left_panel, text="View All Books",
           style="Action.TButton",
           command=view_all_books).pack(pady=10)

ttk.Button(right_panel, text="View All Users",
           style="Action.TButton",
           command=view_all_users).pack(pady=10)

# ================= FORMS =================
def open_add_book():
    win, card = create_form_window("Add New Book")

    ttk.Label(card, text="Book Title").pack(anchor="w")
    title = ttk.Entry(card)
    title.pack(fill="x", pady=5)
    title.bind("<Return>", focus_next_widget)

    ttk.Label(card, text="Author Name").pack(anchor="w")
    author = ttk.Entry(card)
    author.pack(fill="x", pady=5)
    author.bind("<Return>", focus_next_widget)

    ttk.Label(card, text="Number of Copies").pack(anchor="w")
    copies = ttk.Entry(card)
    copies.pack(fill="x", pady=5)

    def submit(event=None):
        try:
            msg = lib.add_book(title.get(), author.get(), int(copies.get()))
            refresh_books_preview()
            messagebox.showinfo("Success", msg)
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    copies.bind("<Return>", submit)

    ttk.Button(card, text="Add Book",
               style="Action.TButton",
               command=submit).pack(pady=15)

    title.focus()

def open_register_user():
    win, card = create_form_window("Register User")

    ttk.Label(card, text="Student Name").pack(anchor="w")
    name = ttk.Entry(card)
    name.pack(fill="x", pady=5)
    name.bind("<Return>", focus_next_widget)

    ttk.Label(card, text="Grade / Class").pack(anchor="w")
    grade = ttk.Entry(card)
    grade.pack(fill="x", pady=5)

    def submit(event=None):
        try:
            msg = lib.register_user(name.get(), grade.get())
            refresh_users_preview()
            messagebox.showinfo("Success", msg)
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    grade.bind("<Return>", submit)

    ttk.Button(card, text="Register User",
               style="Action.TButton",
               command=submit).pack(pady=15)

    name.focus()

def open_issue_book():
    win, card = create_form_window("Issue Book")

    ttk.Label(card, text="Book ID").pack(anchor="w")
    book = ttk.Entry(card)
    book.pack(fill="x", pady=5)
    book.bind("<Return>", focus_next_widget)

    ttk.Label(card, text="User ID").pack(anchor="w")
    user = ttk.Entry(card)
    user.pack(fill="x", pady=5)

    def submit(event=None):
        try:
            msg = lib.issue_book(book.get(), user.get())
            refresh_books_preview()
            messagebox.showinfo("Success", msg)
            win.destroy()
        except BooknotAvailbleError as e:
            messagebox.showerror("Error", str(e))

    user.bind("<Return>", submit)

    ttk.Button(card, text="Issue Book",
               style="Action.TButton",
               command=submit).pack(pady=15)

    book.focus()

def open_return_book():
    win, card = create_form_window("Return Book")

    ttk.Label(card, text="Book ID").pack(anchor="w")
    book = ttk.Entry(card)
    book.pack(fill="x", pady=5)
    book.bind("<Return>", focus_next_widget)

    ttk.Label(card, text="User ID").pack(anchor="w")
    user = ttk.Entry(card)
    user.pack(fill="x", pady=5)

    def submit(event=None):
        try:
            msg = lib.return_book(book.get(), user.get())
            refresh_books_preview()
            messagebox.showinfo("Info", msg)
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    user.bind("<Return>", submit)

    ttk.Button(card, text="Return Book",
               style="Action.TButton",
               command=submit).pack(pady=15)

    book.focus()

# ================= HEADER BUTTONS =================
ttk.Button(btn_frame, text="Add Book",
           style="Action.TButton",
           command=open_add_book).pack(side="left", padx=5)

ttk.Button(btn_frame, text="Register User",
           style="Action.TButton",
           command=open_register_user).pack(side="left", padx=5)

ttk.Button(btn_frame, text="Issue Book",
           style="Action.TButton",
           command=open_issue_book).pack(side="left", padx=5)

ttk.Button(btn_frame, text="Return Book",
           style="Action.TButton",
           command=open_return_book).pack(side="left", padx=5)

# ================= START =================
refresh_books_preview()
refresh_users_preview()
root.mainloop()
