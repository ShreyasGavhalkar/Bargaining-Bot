import pickle
import pdb
import numpy as np
import pandas as pd
import random

class engine:

    def __init__(self,CustomerID):
        self.model = pickle.load(open("/home/shreyas/Documents/Code/Bargaining-Bot/model/model.pkl","rb"))
        self.CustomerID = CustomerID
        self.product_names = ["T-Shirt","Jeans","Socks","Sweater"]

    def _get_price(self,discount,mrp):
        return (1-(discount/100))*mrp

    def _generate_offer(self,quoted_price,discount,mrp):

       
        discount_25 = 0.25*discount
        discount_50 = 0.5*discount 
        discount_75 = 0.75*discount 
        discount_100 = discount

        if(quoted_price < self._get_price(discount_100,mrp)):
            return self._get_price(discount_100,mrp)
        elif(quoted_price < self._get_price(discount_75,mrp)):
            return random.randrange(quoted_price,self._get_price(discount_75,mrp))
        elif(quoted_price < self._get_price(discount_50,mrp)):
            return random.randrange(quoted_price,self._get_price(discount_50,mrp))

        elif(quoted_price < self._get_price(discount_25,mrp)):
            return random.randrange(quoted_price,self._get_price(discount_25,mrp))
        else:
            return quoted_price


    def get_counter_offer(self,quoted_price,StockCode,Quantity,CustomerID):
        """ Returns a random counter offer. Factors to keep in mind while making counter offer: 
             1) Quoted price
             2) Max discounted price (quoted price should not be less than max discount price)
             3) MRP
        """
        breakpoint()
        discount = self.model.predict(np.array([[StockCode,Quantity,CustomerID]]))[0]
        #calculate mrp
        df = pd.read_csv("/home/shreyas/Documents/Code/Bargaining-Bot/model/database.csv")
        mrp = max(df[df.StockCode == StockCode].UnitPrice.unique())

        
        if(int(discount) == 0):
            return mrp
       
        else:
            return self._generate_offer(quoted_price,discount,mrp)
            



    
    def get_products(self):
        """ Returns random Products brought before by the Customer. """

        df = pd.read_csv("/home/shreyas/Documents/Code/Bargaining-Bot/model/database.csv")
        df = df[df.CustomerID == self.CustomerID] #Returns the rows with Product ID
        df = df.drop_duplicates(subset = ["StockCode"]) #Hence We can return 5 distinct productIds
        randoms = df.sample(4)

        result_set = dict()

        i = 0;

        newdf = pd.read_csv("/home/shreyas/Documents/Code/Bargaining-Bot/model/database.csv")
        for r in randoms.index:
            mrp = max(newdf[newdf.StockCode == randoms["StockCode"][r]].UnitPrice.unique())
            result_set[self.product_names[i]] = [randoms["StockCode"][r],mrp]
            i+=1

        return result_set;



a = engine(1780)
a.get_products()


