# KP, Function Notes

# Variables go in the top, and functions go after
# Examples of Functions:
# round()
# len()
# print()

# Variable
income = float(input("What is your monthly income?"))
rent = float(input("What is your monthly rent?"))
utilities = float(input("What is your monthly cost for utilities?"))
transportation = float(input("What is your monthly cost for transportation?"))
groceries = float(input("What is your monthly cost for groceries?"))

# Functions
def calc_percent(bill,income):
    return round(bill/income * 100)

print(f"Your rent is ${rent} which is {calc_percent(rent, income)}% of your income.")
print(f"Your utilities is ${utilities} which is {calc_percent(utilities, income)}% of your income.")
print(f"Your transportation is ${transportation} which is {calc_percent(transportation, income)}% of your income.")
print(f"Your groceries is ${groceries} which is {calc_percent(groceries, income)}% of your income.")
print(f"You should save ${round(income*.1,2)} which is 10% of your income.")
print(f"That means you have ${round(income-(rent+utilities+transportation+groceries),2)} to spend")

# Function Breakdown
# def = define
# def starts every function.
# You then have to name your funciton.
# You then have to put ().
# Inside the (), we put parameters.  
# Parameters are information needed for the function to run.
# Bill and Income are just place holders.
# Parameters are just variables inside and for the function.
# Everything after that is indented is part of the function.
# Return puts the information at the function call.
# {calc_percent(rent,income)} is the function call.
# The (rent,income) are called arguments

# Reasons for Functions:
# To get rid of repetative code
# Helps make code easier to read.
# It keeps our code more organized

def stupid_proof(money):
    while True:
        try:
            temp = float(input(f"What is your monthly {money}: "))
            return temp
        except:
            print("That is not a number :(")

income = stupid_proof("income")
rent = stupid_proof("rent")
utilities = stupid_proof("utilities")
transport = stupid_proof("transport")
groceries = stupid_proof("groceries")
save = round(income*.1,2)



