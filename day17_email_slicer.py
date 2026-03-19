# Day 17 - Email Slicer Tool

print("=== Email Slicer ===")

email = input("Enter your email: ")

# Find position of @
at_index = email.index("@")

username = email[:at_index]
domain = email[at_index + 1:]

print("\nUsername:", username)
print("Domain:", domain)
