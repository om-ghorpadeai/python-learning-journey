# Day 16 - Random Username Generator

import random

print("=== Random Username Generator ===")

name = input("Enter your name: ")

numbers = random.randint(100, 999)

usernames = [
    name + str(numbers),
    name + "_dev" + str(numbers),
    name + "_ai" + str(numbers),
    name + "_coder" + str(numbers),
]

print("\nHere are some username ideas:")

for username in usernames:
    print(username)
