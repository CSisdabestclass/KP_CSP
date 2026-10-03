# KP, Hangman

import random

with open("words.txt", "r") as file:
    words = file.read().splitlines()

secret_word = random.choice(words)

try:
    with open("stats.txt", "r") as file:
        stats = file.read().split(",")

    wins = int(stats[0])
    losses = int(stats[1])

except FileNotFoundError:
    wins = 0
    losses = 0 

wrong_guesses = 0
guessed_letters = []

def show_word(secret_word, guessed_letters):
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_"

        return display_word

def show_hangman(wrong_guesses): 
    if wrong_guesses == 0:
        print("""
   ______
   |    |
   |   
   |   
   |   
   |________
""")

    elif wrong_guesses == 1:
        print("""
   ______
   |    |
   |    O
   |   
   |   
   |________
""")