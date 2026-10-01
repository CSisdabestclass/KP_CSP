# KP, Caesar Cipher

e_d = input("Would you like to (E)ncrypt or (D)ecrypt a message?: ")
message = input("Enter your message: ")
shift = int(input("Enter a shift amount: "))

def cipher(message,shift):
    for letter in message:
        if letter.isalpha():
            number = ord(letter)
            message += shift
            print(f"Your encrypted message is: {chr(message)}")

cipher_1 = cipher("message")   
