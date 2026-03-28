# Day 25 - Improved Result Management System

def add_result():
    print("\n--- Add Student Result ---")
    
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

    with open("result.txt", "a") as file:
        file.write(f"\n{'='*30}\n")
        file.write(f"Name: {name}\n")
        file.write(f"Total Marks: {total}\n")
        file.write(f"Percentage: {percentage:.2f}%\n")
        file.write(f"Grade: {grade}\n")

    print("\n✅ Result saved successfully!")

def view_results():
    print("\n--- View All Results ---")

    try:
        with open("result.txt", "r") as file:
            content = file.read()

            if content:
                print(content)
            else:
                print("No results found.")

    except FileNotFoundError:
        print("No result file found.")

while True:
    print("\n" + "="*40)
    print("   🎓 RESULT MANAGEMENT SYSTEM")
    print("="*40)
    print("1. Add Result")
    print("2. View Results")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_result()

    elif choice == "2":
        view_results()

    elif choice == "3":
        print("\nExiting program... Goodbye Om 👋")
        break

    else:
        print("Invalid choice. Try again.")
