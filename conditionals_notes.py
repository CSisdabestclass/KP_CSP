# KP, Conditional Notes

military_time = 900

if military_time < 600:
    print("Its too early! Why are you awake?")
elif military_time < 900:
    print("Good Morning!")
elif military_time > 1200:
    print("Good Morning! You should be at school!")
elif military_time < 1700:
    print("Good Afternoon!")
else:
    print("Good Evening!")

# A conditional is a block of code that checks to see if some coditions are met and provideds certain outputs if the conditions are met.
# Conditionals always begin with if (Key word).
# Boolean Statement is just an equations that results into true or false.
# We must end a line with a colon if we are using a Conditional.
# If there is a colon, the next line of code must be indented.
# < and > are Comparison Operators.
# Comparison Operators are inequality symbols.
# >= is greater than or equal to.
# < is less than
# > is greater than
# <= is less than or equal to.
# = checks if things are equal
# === checks if things are equal or the same data type.
# != checks if things are not equal
# ! means not in coding
# and, or, not are Logical Operators.
# and is used to add information and both of the conditions have to be met. (Python only)
# or is saying only one of the conditions have to be met. (Python only)
# not is used at the begining to see if it is not true and when the condition is not met. (Python only)
# elif will only check another condition if the condition above it is false.
# else is what happens when nothing above it is true.
# other programing languages don't indent
# Nesting is when you put something in itself.
 
# Nesting Conditionals
day = "Saturday"
time = 900

if time > 900 and time < 1600:
    if day != "Saturday" or day != "Sunday":
        print("You should be at school!")
    else:
        if time > 1200:
            print("Good Afternoon!")
        else:
            print("Good Morning!")
else:
    print("You are not required to be at school!")
