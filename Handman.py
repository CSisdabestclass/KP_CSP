# KP, Hangman

import random

with open('words.txt',"r") as file:
    words = file.read().split(",")

with open("stats.txt", "r") as file:
    file.read().split(",")
    right = 0
    wrong = 0

secret_word = random.choice(words)



for letter in secret_word:
   
    

   

