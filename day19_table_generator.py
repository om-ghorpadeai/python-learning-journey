# Day 19 - Multiplication Table Generator

print("=== Multiplication Table Generator ===")

num = int(input("Enter a number: "))

print("\nTable of", num)

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
