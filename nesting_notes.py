#KP, Nesting Notes
#Nesting is when you put one block of code inside another block of code.
csp = ["Remy", "Alex", "Gabes", "Bliss", "Elsie", "Ivan", "Caydon", "Kaylee", "Levi", "Masen", "William", "Carrera", "Jacob", "Selena", "Ansley,", "Kristian"]
if len(csp) > 0:
    for student in csp:
        print(f"Checking in {student}")
else:
    print("There is no one in htis class.")


while True:
    username = input("What is your username: ").strip()
    password = input("What is your password: ").strip()

    if username == "LaRose4" and password == "password":
        print("Welcome to the program!")
        break
    else:
        print("Those credentials were incorrect.")