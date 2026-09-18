# KP Your Budget 

from unicodedata import numeric

while True:
    try:
        income = float(input("What is your monthly income?:"))
        break
    except:
        print("It has to be a number.")

while True:
    try:
        rent = float(input("What is your monthly rent?:"))
        break
    except:
        print("It has to be a number.")

while True:
    try:
        utilities = float(input("What is your monthly price for utilities?:"))
        break
    except:
        print("It has to be a number.")

while True:
    try:
        groceries = float(input("What is your monthly groceries?:"))
        break
    except:
        print("It has to be a number.")

while True:
    try:
        transportation = float(input("What is your monthly price for transportation?:"))
        break
    except:
        print("It has to be a number.")


print(f"Your rent is ${rent} and that is {rent/income*100}% of your income.")
print(f"Your utilities are ${utilities} and that is {round(utilities/income*100,0)}% of your income.")
print(f"Your groceries is ${groceries} and that is {round(groceries/income*100,0)}% of your income.")
print(f"Your transportation is ${transportation} and that is {round(transportation/income*100,0)}% of your income.")
print(f"You should save ${round(income/10,2)} a month. That is 10& of your income.")
print(f"You have ${round(income-(rent+transportation+groceries+utilities+income/10),2)} of spending money each month!")