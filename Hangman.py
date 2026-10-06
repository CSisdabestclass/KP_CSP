# KP, Hangman

import random

with open("words.txt", "r") as file:
    words = file.read().split(",")

try:
    with open("stats.txt", "r") as file:
        stats = file.read().split(",")

    wins = int(stats[0])
    losses = int(stats[1])

except FileNotFoundError:
    wins = 0
    losses = 0 

secret_word = random.choice(words)

wrong_guesses = 0
guessed_letters = []

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

    elif wrong_guesses == 2:
            print("""
       ______
       |    |
       |    O
       |    |
       |   
       |________
    """)

    elif wrong_guesses == 3:
        print("""
       ______
       |    |
       |    O
       |   /|
       |   
       |________
    """)

    elif wrong_guesses == 4:
        print("""
       ______
       |    |
       |    O
       |   /|\\
       |   
       |________
    """)

    elif wrong_guesses == 5:
        print("""
       ______
       |    |
       |    O
       |   /|\\
       |   /
       |________
    """)

    elif wrong_guesses == 6:
        print("""
       ______
       |    |
       |    O
       |   /|\\
       |   / \\
       |________
    """)


def show_word(secret_word, guessed_letters):
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    return display_word


while True:

    show_hangman(wrong_guesses)

    print("Word:", show_word(secret_word, guessed_letters))
    print("Guessed letters:", guessed_letters)
    print("Wrong guesses remaining:", 6 - wrong_guesses)

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess not in secret_word:
        wrong_guesses += 1
        print("Sorry,", guess.upper(), "is not in the word.")
    else:
        print("Nice!", guess.upper(), "is in the word!")

    if "_" not in show_word(secret_word, guessed_letters):
        print("Congratulations! You guessed the word:", secret_word.upper())

        wins += 1

        with open("stats.txt", "w") as file:
            file.write(str(wins) + "," + str(losses))

        print("Updated Stats - Wins:", wins, "Losses:", losses)

        break

    if wrong_guesses == 6:
        print("You lost!")
        print("The word was:", secret_word.upper())

        losses += 1

        with open("stats.txt", "w") as file:
            file.write(str(wins) + "," + str(losses))

        print("Updated Stats - Wins:", wins, "Losses:", losses)

        break