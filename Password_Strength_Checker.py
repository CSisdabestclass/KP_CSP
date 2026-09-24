# KP, Password Strength Checker

password = input("Please give me your password:")

uppercase = False
lowercase = False
Length = False
number = False
symbol = False
strength = 0

for letter in password:
    if letter.isupper():
        uppercase=True
    if letter.islower():
        lowercase=True
    if len(password)>=8:
        Length = True
    if letter.isnumeric():
        number = True
    if letter in "!@#$%^&*":
        symbol = True

score = 0
if uppercase == True:
    score+=1
if lowercase == True:
    score+=1
if Length == True:
    score+=1
if number == True:
    score+=1
if symbol == True:
    score+=1

if score == 5:
    strength = "Strong"
if score ==4:
    strength = "Medium"
if score == 3:
    strength = "Medium"
if score == 2:
    strength = "Weak"
if score == 1:
    strength = "Weak"

improve = 







print(f"At least 8 characters: {Length}")
print(f"Has an uppercase letter: {uppercase}")
print(f"Has a lowercase letter: {lowercase}")
print(f"Has a number: {number}")
print(f"Has a symbol: {symbol}")
print(f"Your password strength is: {strength}")
print(f"To make it Strong, add: {improve}")