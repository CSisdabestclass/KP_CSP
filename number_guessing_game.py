# KP Number Guessing Game
import random

number = random.randint(1,100)
score = 0
right = 0
guess0 = 0
while right == 0:
    guess = int(input("Guess #1: "))
    if guess > number:
        print("Too High!")
        score +1
    if guess < number:
        print ("Too Low!")
        score +1
    if guess == number:
        print(f"You got it! It took you {score} try(s)!")
        right +1



