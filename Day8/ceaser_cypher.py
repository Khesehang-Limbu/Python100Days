import ceaser_cypher_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cypher(text, shift, direction):
    cypher_text = ""
    if direction == "decode":
        shift *= -1
    if shift > 2:
        shift %= 26
    for i in range(len(text)):
        text = list(text) 
        if text[i] in alphabet:
            current_index = alphabet.index(text[i]) #7   
            if current_index + shift > 25:
                current_index = 0
            if (current_index == 0 and text[i] != "a"):
                text[i] = alphabet[current_index + shift-1]
            else:
                text[i] = alphabet[current_index + shift]
        cypher_text += text[i]
    return cypher_text

isFinished = False

print(ceaser_cypher_art.logo)


while not isFinished:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        print(f"The encoded text is {cypher(text=text, shift=shift, direction=direction)}")
    elif direction == "decode":
        print(f"The decoded text is {cypher(text=text, shift=shift, direction=direction)}")
    else:
        print("Invalid Input")
    
    continuation = input("Do You want to continue? press Y or N : ").lower()
    if (continuation == "n"):
        isFinished = True
        print("Goodbye")