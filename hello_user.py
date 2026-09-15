# KP, Hello User
while True: 
    name = input("What is your name?: ").strip().capitalize()
    if name.isnumeric():
        print("It can't have a number!")
    elif " " in name:
        print("Only your first name.")
    else:
        break

print(f"Hello {name}!")