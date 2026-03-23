# Day 20 - Simple Login System

print("=== Login System ===")

correct_username = "om"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login Successful ✅")
else:
    print("Invalid username or password ❌")
