print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to the Treasure Island Game!!")
print("Your mission is to find the treasure")
cross_road = input("You're at a cross-road, where do you want to go? left or right? ").lower()

if (cross_road == "left"):
    lake = input('You havve come to a lake. There is an island in the middle of the lake, type "wait" to wait for a boat or "swim" to swim ').lower()
    if (lake == "wait"):
        room = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if (room == "yellow"):
            print("You found the treasure, You Win!!")
        elif (room == "red"):
            print("The room was full of lava, you fell into the lava and died. Game OVer!!")
        else:
            print("The room is full of poison gas. You died. Game Over")
    else:
        print("You tried to swim through a river full of crocodiles, they ate you. Game Over!!")
else:
    print("The Earth is shattering, you fell off a clip and died. Game Over!!")