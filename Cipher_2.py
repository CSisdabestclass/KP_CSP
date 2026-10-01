# KP, Caesar Cipher

e_d = input("Would you like to (E)ncrypt or (D)ecrypt a message?: ")
message = input("Enter your message: ")
shift = int(input("Enter a shift amount: "))


def caesar_cipher(message,shift):
    result = ""

    for letter in message:
        if letter.isalpha():
            number = ord(letter)

            if letter.isupper():
                start = ord("A")
            else:
                start = ord("a")

            position = number - start
            position_2 = (position + shift) % 26
            letter_1 = chr(start + position_2)

            result += letter_1
        else:
            result += letter

    return result

if e_d == "E":
    result = caesar_cipher(message, shift)
    print(f"Your encrypted message is: {result}")
elif e_d == "D":
    result = caesar_cipher(message, -shift)
    print(f"Your decrypted message is: {result}")

