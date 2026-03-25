# Day 22 - Result Analyzer with File Saving

print("=== Student Result Analyzer ===")

name = input("Enter student name: ")

marks = []
subjects = 5

for i in range(subjects):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / subjects

# Grade system
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

# Display result
print("\n--- Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)

# Save to file
file = open("result.txt", "a")

file.write(f"\nName: {name}\n")
file.write(f"Total: {total}\n")
file.write(f"Percentage: {percentage}\n")
file.write(f"Grade: {grade}\n")
file.write("----------------------\n")

file.close()

print("\nResult saved to file successfully 📁")
