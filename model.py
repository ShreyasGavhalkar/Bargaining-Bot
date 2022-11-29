import pickle
import pdb
import numpy as np
import pandas as pd

class engine:

    def __init__(self):
        self.model = pickle.load(open("model.pkl","rb"))
        self.SC = dict()
        self.product_names = ["T-Shirt","Jeans","Socks","Sweater"]

    def get_counter_offer(self,quoted_price,product_name,Quantity,CustomerID):
        """ Returns a random counter offer. Factors to keep in mind while making counter offer: 
             1) Quoted price
             2) Max discounted price (quoted price should not be less than max discount price)
             3) MRP
        """
        StockCode = self.SC[product_name]
        discount = self.model.predict(np.array([[StockCode,Quantity,CustomerID]]))

    
    def get_products(self,CustomerID):
        """ Returns random Products brought before by the Customer. """

        df = pd.read_csv("database.csv")
        df = df[df.CustomerID == CustomerID] #Returns the rows with Product ID
        df = df.drop_duplicates(subset = ["StockCode"]) #Hence We can return 5 distinct productIds
        randoms = df.sample(4)

        result_set = dict()

        i = 0;

        for r in randoms.index:
            result_set[self.product_names[i]] = [randoms["StockCode"][r],randoms["UnitPrice"][r]]
            i+=1

        return result_set;


                



a = engine()
res = a.get_products(17850)
print(res)
