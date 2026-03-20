# Day 18 - Number Checker Tool

print("=== Number Checker ===")

num = int(input("Enter a number: "))

# Check positive / negative / zero
if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

# Check even or odd
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
