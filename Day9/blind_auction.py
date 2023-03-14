from blind_auction_art import logo
import os

print(logo)

participants = []
auction = {}

def storing_bids(name, bid):    
    auction["name"] = name
    auction["bid"] = bid
    return participants.append(auction)

isTrue = False
max_bid = 0
winner = ""
while not isTrue:
    bidder_name = input("Enter your name : ")
    bid = int(input("Enter the bid : $"))

    storing_bids(bidder_name, bid)
    
    for i in range (len(participants)):
        if participants[i]["bid"] > max_bid:
            max_bid = participants[i]["bid"]   
            winner += participants[i]["name"]

    decision = input("Are there any bidders? Y or N ").lower()
    if decision == 'n':
        isTrue = True

    os.system("cls")

print(f"The winner is {winner} with the bid of ${max_bid}")

