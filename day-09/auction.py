from os import system
from art import header
bidders = {}

def main():
    welcome()
    check_bidder()
    another_bidder()

def welcome():
    print(header)

def bidder():
    a = input("👤 What's Your Name? ")
    b = input("💵 How much do you want to bid? $")

    return a , b

def check_bidder():
    name , bid = bidder()
    bidders[name] = int(bid)
    print(f"✅ {name} registered with bid of ${bid}")

def bidder_amount():
    compare = 0
    for key in bidders:
        if bidders[key] > compare:
            compare = bidders[key]
    
    print(f"{key} is the largest bidder with ${compare}")
           
def another_bidder():
    while True:
        ask = input("❓ Is there another bidder? (Yes/No): ").lower()

        if ask == "yes":
            print("🔄 Adding another bidder...\n")
            system("cls")
            check_bidder()
        else:
            print("🏁 Auction ending... Calculating results!")
            bidder_amount()
            break    
main()