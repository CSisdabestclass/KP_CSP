# KP, Loop Notes

# code that will repeat over and over again.
import random
count = 1

while count <= 10:
    print(count)
    count += 1

# There are 3 steps in a loop. (start point, stop point and iterator).
# count = 1 is the start point.
# count <= 10 is our stop point (booleon statement).
# count += 1 is the iterator.
# the iterator keeps track of our iteration.
# the iteration is the one instance in the loop.
# while is the key word that starts the while loop.
# += increases the variable and resets the value.

goose = random.randint(1,11)
ducks = 1

while True:
    print("duck")
    ducks += 1
    if ducks == goose:
        break
print("GOOSE!!!!")

# continue will stop the iteration and bring you back to the begining.
# Lists are serounded by brakets.
# Every item in your list must be seperated by a comma.
# Every item in your list must have the correct data type.
siblings = ["Isabella", "Julia", "Noemi"]