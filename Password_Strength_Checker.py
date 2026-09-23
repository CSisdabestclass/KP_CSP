# KP, Password Strength Checker

password = input("Please give me your password:")

if len(password) >= 8:
    length = True
else:
    length = False

for letter in password:
    if password.upper:
        uppercase = True
    else:
        uppercase = False


if password.islower():
    lowercase = True
else:
    lowercase = False

if password.isnumeric:
    number = True
else:
    number = False

if password in "!@#$%^&*":
    symbol = True
else:
    symbol = False












print(f"At least 8 characters: {length}")
print(f"Has an uppercase letter: {uppercase}")
print(f"Has a lowercase letter: {lowercase}")
print(f"Has a number: {number}")
print(f"Has a symbol: {symbol}")
