#basic input and output
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from model.model import engine
# from . import guitest
if __name__ == '__main__':
    # buying_price = 300 #in rupees
    # selling_price = 1000 #in rupees

    # gametree = GameTree(buying_price, selling_price)

    # while True:
    #     offer = int(input("Give me an offer"))
    #     ans = gametree.check_offer(offer)
    #     if(ans):
    #         print("Fine that woks")
    #         break
    #     elif(not ans):
    #         print("Sorry no deal")
    #     else:
    #         print("Lets see if we can do better")
    engine_obj = engine(4016)
    bot  = ChatBot("Bargainer")
    list_t = ListTrainer(bot)
    list_t.train([
    "Hi",
    "Welcome",
    ])
    list_t.train(["Yes", "Great, that works!"])
    list_t.train(["No", "Let me see what I can do"])
    list_t.train(["ask for offer", "Give me a quote price: "])
    list_t.train(["finish", "I dont think this negotiation is going anywhere, bye"])
    list_t.train(["end chat", "Glad we could agree!\nBye!"])
    list_t.train(["offer", "Here is my offer for you: "])
    list_t.train(["choose", "Do you accept this offer? (yes/no): "])
    flag = 1
    counter_offer_counter = 0
    products = engine_obj.get_products()
    print("Here are the products I have\n", products)
    interested_product = input("Enter the product name of the interested product: ")
    interested_product = products[interested_product]
    ans = input("The price of the product is: "+str(interested_product[1])+" Is this fine?(yes/no)")
    if(ans=="yes"):
        flag = 0
        print("Thanks!")
        exit()
    else:
        while flag:
            quote = float(input(bot.get_response("ask for offer")))
            counter = engine_obj.get_counter_offer(quote, interested_product[0], 1, 1780)
            if(counter==-1 or counter_offer_counter>10):
                print(bot.get_response("finish"))
                exit()
            else:
                print(bot.get_response("offer"),": ",counter)
                ans = input(bot.get_response("choose"))
                if ans=="yes":
                    print(bot.get_response("end chat"))
                    exit()
                else:
                    counter_offer_counter+=1


            




    

