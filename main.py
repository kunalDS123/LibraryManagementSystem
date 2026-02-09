from library import Library,BooknotAvailbleError

lib = Library()

while True:
    print("\n===== SMART LIBRARY =====")
    print("1. Add Book")
    print("2. Register User")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Users")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    try:
        if choice == 1:
            lib.add_book()
        elif choice == 2:
            lib.regester_user()
        elif choice == 3:
            lib.issue_book()
        elif choice == 4:
            lib.return_book()
        elif choice == 5:
            lib.view_books()
        elif choice == 6:
            lib.view_users()
        elif choice == 7:
            print("Exiting System")
            break
        else:
            print("Invalid choice!")
            
    except BooknotAvailbleError as e:
        print("Error",e)
    except Exception as e:
        print("Unexpected error" , e)

