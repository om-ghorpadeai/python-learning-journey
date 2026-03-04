# Day 7 - Number Guessing Game

print("=== Number Guessing Game ===")

secret_number = 7
attempts = 0

while True:
    guess = int(input("Guess the number between 1 and 10: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("Correct! 🎉")
        print("You guessed it in", attempts, "attempts.")
        break
