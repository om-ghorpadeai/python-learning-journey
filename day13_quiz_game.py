# Day 13 - Quiz Game

print("=== Python Quiz Game ===")

score = 0

print("\nQuestion 1: What does CPU stand for?")
answer = input("Your answer: ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nQuestion 2: Which language are we learning?")
answer = input("Your answer: ")

if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nQuestion 3: What symbol is used for comments in Python?")
answer = input("Your answer: ")

if answer == "#":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nQuiz finished!")
print("Your score:", score, "/ 3")
