# Day 28 - Expense Tracker

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    with open("expenses.txt", "a") as file:
        file.write(f"{name},{amount}\n")

    print("Expense added successfully 💰")

def view_expenses():
    total = 0

    try:
        with open("expenses.txt", "r") as file:
            print("\n--- Expenses ---")

            for line in file:
                name, amount = line.strip().split(",")
                amount = float(amount)
                total += amount
                print(f"{name}: ₹{amount}")

        print("\nTotal Spending: ₹", total)

    except FileNotFoundError:
        print("No expenses found.")

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Exiting... 👋")
        break

    else:
        print("Invalid choice")
