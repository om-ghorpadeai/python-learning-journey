# Day 21 - Student Result Analyzer (Advanced)

print("=== Student Result Analyzer ===")

name = input("Enter student name: ")

marks = []
subjects = 5

for i in range(subjects):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / subjects

print("\n--- Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

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

print("Grade:", grade)
print("Keep working hard, Om 💪")
