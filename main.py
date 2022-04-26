from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction.")

bids = {} # empty list
bidding_finished = False

def find_highest_bidder(bidding_record): #bidding_record is bids
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid of {highest_bid}")        

while not bidding_finished:
    name = input("what is your name?: ")
    price = int(input("what is your bid?: "))
    bids[name] = price #adds the values to the dictionary
    should_continue = input("are there any others to bid? Type 'yes' or 'no' ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids) #trigger our funcrion with bids dictionary
    elif should_continue == "yes":
        clear() #clear the screen and input new bidder   
