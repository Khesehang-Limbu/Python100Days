import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand_symbols = [rock, paper, scissors]
computer_symbol = random.randint(0, 2)

user_symbol = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors : "))
if (user_symbol >= 3):
    print("Invalid Input, You Lose")
    exit()
print(hand_symbols[user_symbol])

print("Computer Choose : ")
print(hand_symbols[computer_symbol])


if ((user_symbol == 0 and computer_symbol == 2) or (user_symbol == 1 and computer_symbol == 0) or (user_symbol == 2 and computer_symbol == 1)):
    print("You Win")
elif ((user_symbol == 0 and computer_symbol == 1) or (user_symbol == 1 and computer_symbol == 2) or (user_symbol == 2 and computer_symbol == 0)):
    print("You Lose")
else:
    print("Draw")

