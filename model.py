import pickle
import pdb
import numpy as np
import pandas as pd

class engine:

    def __init__(self,CustomerID):
        self.model = pickle.load(open("model.pkl","rb"))
        self.CustomerID = CustomerID
        self.product_names = ["T-Shirt","Jeans","Socks","Sweater"]

    def _generate_offer(self,quoted_price,discounted_price,mrp):
        return (quoted_price + discounted_price)/2;


    def get_counter_offer(self,quoted_price,StockCode,Quantity,CustomerID):
        """ Returns a random counter offer. Factors to keep in mind while making counter offer: 
             1) Quoted price
             2) Max discounted price (quoted price should not be less than max discount price)
             3) MRP
        """

        discount = self.model.predict(np.array([[StockCode,Quantity,CustomerID]]))
        
        #calculate mrp
        df = pd.read_csv("database.csv")
        mrp = max(df[df.StockCode == StockCode].UnitPrice.unique())
        discounted_price = (1-(discount/100))*mrp

        
        if(quoted_price<=discounted_price):
            return -1;
       
        else:
            return self._generate_offer(quoted_price,discounted_price,mrp)
            



    
    def get_products(self):
        """ Returns random Products brought before by the Customer. """

        df = pd.read_csv("database.csv")
        df = df[df.CustomerID == self.CustomerID] #Returns the rows with Product ID
        df = df.drop_duplicates(subset = ["StockCode"]) #Hence We can return 5 distinct productIds
        randoms = df.sample(4)

        result_set = dict()

        i = 0;

        for r in randoms.index:
            mrp = max(df[df.StockCode == randoms["StockCode"][r]].UnitPrice.unique())
            result_set[self.product_names[i]] = [randoms["StockCode"][r],mrp]
            i+=1

        return result_set;


                



a = engine(17850)
res = a.get_products()
print(res)
