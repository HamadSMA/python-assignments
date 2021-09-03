from replit import clear
from art import logo

highest_bidder = 0
winner = ""
auction = {}
end = False
invalid = False
print(logo)
print("Welcome to the secret auction")

while not end:
    name = input("Please type in your name: ")
    bid = int(input("Please enter you bid: $"))
    auction[name]=bid
    answer = input("Are there more bidders? type 'yes' or 'no'").lower()
    if answer == "no":
        end = True
    elif answer == "yes":
        clear()
        end = False

for bidder in auction:
    if auction[bidder] > highest_bidder:
         winner = bidder
         highest_bidder = auction[bidder]

print(f"The winner is {winner} with a bid of ${highest_bidder}")
