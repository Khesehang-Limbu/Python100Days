#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# all_names = []
new_names = []
with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as data:
    all_names = data.readlines()

for name in all_names:
    new_names.append(name.strip())
# print(new_names)

# for name in new_names:
#     with open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", "w") as data:
#         with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", "r+") as line:
#             lines = line.readlines()
#             x = "".join(lines).replace("[name]", name)
#             data.write(x)

for name in all_names:
    stripped_name = name.strip()
    with open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as data:
        with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", "r+") as line:
            lines = line.read()
            new_letter = "".join(lines).replace("[name]", stripped_name)
            data.write(new_letter)


