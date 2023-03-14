from art import logo
import random
import os

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

# print(logo)
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# def deal_card():
#     random_cards = []
#     first_card = random.choice(cards)
#     random_cards.append(first_card)
    
#     if 11 in random_cards:
#         second_card = 1
#         random_cards.append(second_card)
#     else:
#         random_cards.append(random.choice(cards))
#     return random_cards

# player_cards = deal_card()
# computer_cards = deal_card()

# print(f"Your cards : {player_cards}, current score : {player_cards[0] + player_cards[1]}")
# print(f"Computer's first card : {computer_cards[0]}")
# user_choice = input("Press 'y' to get another card or 'n' to pass : ").lower()

# if (user_choice == 'y'):
#     pick_another_card = True
    
#     while (pick_another_card):
#         new_card = player_cards.append(random.choice(cards))
#         sum = 0
#         for card in player_cards:
#             sum += card
#             if (sum > 21 and card == 11):
#                 card =1
        
#         if (sum > 21):
#             print(f"Your cards : {player_cards}, current score : {sum}")
#             print(f"Computer's first card : {computer_cards[0]}")
#             print("You went over 21, you Lose")
#             pick_another_card = False
#         elif (sum == 21):
#             print(f"Your cards : {player_cards}, current score : {sum}")
#             print(f"Computer's first card : {computer_cards[0]}")
#             print("Blackjack, You Win")
#             pick_another_card = False
#         else:
#             print(f"Your cards : {player_cards}, current score : {sum}")
#             print(f"Computer's first card : {computer_cards[0]}")
#             user_choice = input("Press 'y' to get another card or 'n' to pass : ").lower()
#             if (user_choice == 'n'):
#                 pick_another_card = False
                
# if (user_choice == 'n'):
#     shouldContinue = False
#     user_score = 0 
#     computer_score = 0
    
#     for card in player_cards:
#         user_score += card
    
#     for card in computer_cards:
#         computer_score += card 
                
#     print(f"Your cards : {player_cards}, current score : {user_score}")
#     print(f"Computer's cards : {computer_cards}, computer score : {computer_score}")
    
#     if (user_score > computer_score):
#         print("You Win.")
#     elif(user_score == computer_score):
#         print("Draw")
#     else:
#         print("You Lose")
     
#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   
# def deal_card():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     return random.choice(cards)

# #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
# #and returns the score. 
# #Look up the sum() function to help you do this.
# def calculate_cards(cards):
#     #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
#     if (sum(cards) == 21 and len(cards) == 2):
#         return 0
#     #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
#     if (sum(cards) > 21 and (11 in cards)):
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)

# #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
# def compare(user_score, computer_score):
#     if user_score > 21 and computer_score > 21:
#          return "You went over. You lose 😭"
     
#     if (user_score == 0):
#         return "Win with a Blackjack 😎"
#     elif (computer_score == 0):
#         return "Lose, opponent has Blackjack 😱"
#     elif (computer_score == user_score):
#         return "Draw 🙃"
#     elif user_score > 21:
#         return "You went over. You lose 😭"
#     elif ( computer_score > 21):
#         return "Opponent went over. You win 😁"
#     elif (computer_score < user_score):
#         return "You win 😃"
#     else:
#         return "You lose 😤"
     
# #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# #user_cards = []
# #computer_cards = []
   
# user_cards = []
# computer_cards = []

# def play_game():
#     os.system("cls")
#     print(logo)
#     for _ in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())
#     is_over = False

#     while not is_over:    
#         user_score = calculate_cards(user_cards)
#         computer_score = calculate_cards(computer_cards)
#         print(f"Your cards : {user_cards}, current score : {user_score}")
#         print(f"Computer's first hand : {computer_cards[0]}")

#         #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_over = True
            
#         #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
#         #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
#         user_choice = input("Press 'y' to get another card or 'n' to pass : ").lower()
#         if (user_choice == "y" and user_score < 21):
#             user_cards.append(deal_card())
#         else:
#             is_over = True

#     #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
#     while (computer_score < 17 and computer_score != 0):
#         computer_cards.append(deal_card())
#         computer_score = calculate_cards(computer_cards)

#     print(f"   Your final hand: {user_cards}, final score: {user_score}")
#     print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
#     print(compare(user_score, computer_score))
    
# #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
# while input("Do you want to play a game of blackjack? y or n : ").lower() == 'y':
#     play_game()

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(logo)

  #Hint 5: Deal the user and computer 2 cards each using deal_card()
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

  while not is_game_over:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system("cls")
  play_game()





#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt



