# Day 14 - Guessing Game with Limited Attempts

import random

print("=== Guess the Number Game ===")

secret_number = random.randint(1, 20)
attempts = 5

while attempts > 0:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts -= 1

    if guess == secret_number:
        print("Congratulations! You guessed the number.")
        break

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")

    print("Attempts left:", attempts)

if attempts == 0:
    print("Game Over! The correct number was:", secret_number)
