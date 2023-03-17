from art import logo, vs
from game_data import data
import random
import os

total = 0

def random_member_generator():
    return random.choice(data)

def compare_followers(user_guess, against):
    global total
    if (user_guess > against["follower_count"]):
        os.system("cls")
        total += 1
        print(f"You're right, current score is {total}")
        return True
    else:
        print(f"Sorry, that's wrong. Final Score : {total}")
        return False
    
    
is_game_over = False
A = random_member_generator()
B = random_member_generator()

while not is_game_over:
    print(logo)
    print(f'Compare A : {A["name"]}, a {A["description"]} from {A["country"]}')
    print(vs)

    print(f'Against B : {B["name"]}, a {B["description"]} from {B["country"]}')
    user_choice = input("Who has more followers? Type 'a' or 'b' : ").lower()
    
    if (user_choice == 'a'):
        user_guess = A["follower_count"]
        if(compare_followers(user_guess, B) == False):
            is_game_over = True
        else:
            A = A
            B = random_member_generator()
    else:
        user_guess = B["follower_count"]
        if(compare_followers(user_guess, A) == False):
            is_game_over = True
        else:
            A = B
            B = random_member_generator()
    