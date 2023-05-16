import random
import hangman_art
import hangman_words
import os

lives = 6
isGameOver = False

random_word = random.choice(hangman_words.word_list)
random_character_list = list(random_word)
hidden_list = []

print(hangman_art.logo)

for character in random_character_list:
    hidden_list.append("_");
print(' '.join(hidden_list))

while (not isGameOver):
    user_input = input("Enter a character : ")
    os.system('cls')
    if user_input in hidden_list:
        print("You already tried that letter, try another..")
    else:    
        for i in range(len(random_character_list)):    
            if random_character_list[i] == user_input:
                hidden_list[i] = user_input
                
        if random_character_list.__contains__(user_input) == 0:
            lives-=1
            print(f"{user_input} is not in the word, you guessed it wrong, you lose a life, now you have {lives}")
            print(hangman_art.stages[lives])
            
        if (lives == 0):
            print(f"You have {lives} lives remaining, you're dead")
            isGameOver = True
                
        if hidden_list.__contains__("_") == False:
            print("Hurray!! you have completed the game...")
            isGameOver = True

    print(' '.join(hidden_list))
        