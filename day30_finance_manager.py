# Day 30 - Personal Finance Manager

def add_income():
    amount = float(input("Enter income amount: "))
    with open("finance.txt", "a") as file:
        file.write(f"Income,{amount}\n")
    print("Income added 💰")

def add_expense():
    amount = float(input("Enter expense amount: "))
    with open("finance.txt", "a") as file:
        file.write(f"Expense,{amount}\n")
    print("Expense added 💸")

def view_records():
    balance = 0
    try:
        with open("finance.txt", "r") as file:
            print("\n--- Records ---")

            for line in file:
                type_, amount = line.strip().split(",")
                amount = float(amount)

                if type_ == "Income":
                    balance += amount
                else:
                    balance -= amount

                print(f"{type_}: ₹{amount}")

        print("\nCurrent Balance: ₹", balance)

    except FileNotFoundError:
        print("No records found.")

while True:
    print("\n=== Personal Finance Manager ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Records")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_income()

    elif choice == "2":
        add_expense()

    elif choice == "3":
        view_records()

    elif choice == "4":
        print("Goodbye Om 👋")
        break

    else:
        print("Invalid choice")
