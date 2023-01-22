

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()

with open("./Input/Names/invited_names.txt") as  file:
    for i in file.read().split("\n"):
        old = letter.replace("[name]", i)
        new = open(f"./Output/ReadyToSend/{i}", "w")
        new.write(old)




