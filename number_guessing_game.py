# KP Number Guessing Game
import random

number = random.randint(1, 100)
right = 0
score = 1

while True:
    guess = int(input(f"Guess #{score}: "))
    
    if guess == number:
        print(f"You got it! It took you {score} try(s)!")
        right += 1
        break
    elif score == 6:
        print(f"You're out of guesses! The number was {number}.")
        break
    elif guess > number:
        print("Too High!")
        score += 1
    else:
        print("Too Low!")
        score += 1


