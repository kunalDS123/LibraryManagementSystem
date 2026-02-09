from gui import root
root.mainloop()


# from library import Library, BooknotAvailbleError

# lib = Library()

# while True:
#     print("\n===== SMART LIBRARY =====")
#     print("1. Add Book")
#     print("2. Register User")
#     print("3. Issue Book")
#     print("4. Return Book")
#     print("5. View Books")
#     print("6. View Users")
#     print("7. Exit")

#     choice = input("Enter choice: ")

#     try:
#         if choice == "1":
#             title = input("Enter book title: ")
#             author = input("Enter author: ")
#             copies = int(input("Enter number of copies: "))
#             print(lib.add_book(title, author, copies))

#         elif choice == "2":
#             name = input("Enter student name: ")
#             grade = input("Enter grade: ")
#             print(lib.register_user(name, grade))

#         elif choice == "3":
#             book_id = input("Enter Book ID: ")
#             user_id = input("Enter User ID: ")
#             print(lib.issue_book(book_id, user_id))

#         elif choice == "4":
#             book_id = input("Enter Book ID: ")
#             user_id = input("Enter User ID: ")
#             print(lib.return_book(book_id, user_id))

#         elif choice == "5":
#             lib.view_books()

#         elif choice == "6":
#             lib.view_users()

#         elif choice == "7":
#             print("Exiting System...")
#             break
#         else:
#             print("Invalid choice!")

#     except BooknotAvailbleError as e:
#         print("Error:", e)

#     except ValueError:
#         print("Invalid input! Please enter correct values.")

#     except Exception as e:
#         print("Unexpected error:", e)
