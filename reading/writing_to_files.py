# KP, Reading and Writing to Files.

with open("reading\practice_file.txt", "r") as file:
    content = file.read()
    print(content)
    word = content.find("Kristian")
    length = len("Kristian")
    content += "trason"
    print(content[word:word+length])
    file.write(content)

with open("reading\practice_file.txt","w") as file:
    file.write("Hello!")
# w means write
# If we have a w, we need to put file.write
# .write replaces everything