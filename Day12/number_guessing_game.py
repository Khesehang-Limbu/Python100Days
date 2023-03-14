from art import logo
import random

EASY_LEVEL = 10
HARD_LEVEL = 5

def set_difficulty():
    user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if user_choice == "easy":
        return EASY_LEVEL
    if user_choice == "hard":
        return HARD_LEVEL

def check_answer(guess, answer):
    if (guess > answer):
        print("Too High")
        return False
    elif (guess < answer):
        print("Too Low")
        return False
    else:
        print(f"You got it, the answer was {answer}")
        return True

def play_game():   
    print(logo)
    answer = random.randint(1, 100)
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
    lives = set_difficulty()

    is_game_over = False
    while not is_game_over:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess : "))
        if check_answer(guess, answer) == True:
            is_game_over = True
        else:
            lives -= 1
            print("Make a guess")
        
        if (lives == 0):
            is_game_over = True
            print("You've run out of guesses, you lose.")

play_game()
    