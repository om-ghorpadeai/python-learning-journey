# Day 8 - Password Strength Checker

print("=== Password Strength Checker ===")

password = input("Enter your password: ")

length = len(password)

if length < 6:
    print("Password strength: Weak ❌")
    print("Try using at least 6 characters.")

elif length < 10:
    print("Password strength: Medium ⚠️")
    print("You can make it stronger.")

else:
    print("Password strength: Strong ✅")
    print("Good password!")

print("Program finished.")
