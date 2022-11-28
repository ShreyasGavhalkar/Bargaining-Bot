#basic input and output
from . import GameTree

if __name__ == '__main__':
    buying_price = 300 #in rupees
    selling_price = 1000 #in rupees

    gametree = GameTree(buying_price, selling_price)

    while True:
        offer = int(input("Give me an offer"))
        ans = gametree.check_offer(offer)
        if(ans):
            print("Fine that woks")
            break
        elif(not ans):
            print("Sorry no deal")
        else:
            print("Lets see if we can do better")
