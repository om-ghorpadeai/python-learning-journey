# Day 15 - Contact Book Program

contacts = {}

while True:
    print("\n=== Contact Book ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")

    elif choice == "2":
        print("\nYour Contacts:")
        for name, phone in contacts.items():
            print(name, "-", phone)

    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            print(search, ":", contacts[search])
        else:
            print("Contact not found.")

    elif choice == "4":
        print("Exiting Contact Book.")
        break

    else:
        print("Invalid choice. Try again.")
