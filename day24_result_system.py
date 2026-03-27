# Day 24 - Result Management System

def add_result():
    name = input("Enter student name: ")

    marks = []
    for i in range(5):
        mark = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

    file = open("result.txt", "a")
    file.write(f"\nName: {name}\n")
    file.write(f"Total: {total}\n")
    file.write(f"Percentage: {percentage}\n")
    file.write(f"Grade: {grade}\n")
    file.write("----------------------\n")
    file.close()

    print("Result saved successfully!")

def view_results():
    try:
        file = open("result.txt", "r")
        content = file.read()

        if content:
            print("\n--- All Results ---")
            print(content)
        else:
            print("No results found.")

        file.close()

    except FileNotFoundError:
        print("No result file found.")

while True:
    print("\n=== Result Management System ===")
    print("1. Add Result")
    print("2. View Results")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_result()
    elif choice == "2":
        view_results()
    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
