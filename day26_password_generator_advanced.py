# Day 26 - Advanced Password Generator

import random
import string

print("=== Advanced Password Generator ===")

length = int(input("Enter password length: "))

use_numbers = input("Include numbers? (yes/no): ").lower()
use_symbols = input("Include symbols? (yes/no): ").lower()

characters = string.ascii_letters

if use_numbers == "yes":
    characters += string.digits

if use_symbols == "yes":
    characters += string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:", password)# Day 26 - Advanced Password Generator

import random
import string

print("=== Advanced Password Generator ===")

length = int(input("Enter password length: "))

use_numbers = input("Include numbers? (yes/no): ").lower()
use_symbols = input("Include symbols? (yes/no): ").lower()

characters = string.ascii_letters

if use_numbers == "yes":
    characters += string.digits

if use_symbols == "yes":
    characters += string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:", password)
