# KP String Notes

# Holds numbers that contain decimals or character or simbles
# Must be surounded by qutation marks or single quotation marks

first_name = 'Vienna'
last_name = 'LaRose'
name = first_name +" " + last_name
# escape char (\) lets the program ignore the next character in the string.
# you can also use back slash (\) without a string.
print(f'{name} told me the class "You can\'t drive my car."')

#concatenation is when you add 2 string together
# " " = space
# f = f string (Formated string)
# f string also lets you use {} in quotation marks.
# We use the f string because its easy to insert variables and easier to specify how it prints for the user.
# {} is used to take a break in the string.
# Strings have something called Methods.
# Methods they allow you to alter or mynipulate a string.
# You write a method by string.name of method ()
# e.g. name.upper()
# e.g. name.capitalize()
# e.g. "tia".capitalize()

user = input("Please tell me your name:\n").strip().title()

print(f"New user recognized\nWelcome {user}")

sentence = "The quick brown fox jumped over the lazy dog."
print(f"The sentence is {len(sentence)} characters long.")
print(sentence)
print(sentence.replace("dog", "cat"))
# \n makes it so when the user types something, it goes to the next line.
# {len(variable)} counts how many characters there are in the sentence.