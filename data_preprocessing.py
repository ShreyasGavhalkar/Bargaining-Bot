import pandas as pd
from sklearn.preprocessing import LabelEncoder
import time


##### UTILITY FUNCTIONS
def discount(mrp,unit_price):
    return ((mrp-unit_price)/(mrp))*100

def mrp(max_unit_price):
    return max_unit_price*1 #can be changed later

def contains_alphabet(stock_code):
    
    for char in stock_code:
        if(char.isalpha()):
            return True;
    return False;

################################

##### Removing nan values and duplicates
df = pd.read_csv("data.csv",encoding = "ISO-8859-1")
df = df.dropna() #drop all Rows with any NaN value
df = df.drop_duplicates() #drops all duplicate rows
################################

###### Removing invalid values
df = df[df.Quantity>0] #Remove Items with a negative Quantity value
df = df[df.UnitPrice>0] #Remove items with Unit price <= zero (Free items)
################################

###### Dropping unwanted columns
df = df.drop('InvoiceNo',axis = 1) #remove un
df = df.drop('InvoiceDate',axis = 1)
df = df.drop('Country',axis = 1)
df = df.drop('Description',axis = 1)
################################


###### Removing StockCodes with alphabets in them
stock_codes = list(df.StockCode.unique())
code_maxp = dict()

for stock in stock_codes:
        code_maxp[stock] = mrp(max(df[df.StockCode == stock].UnitPrice.unique()))

################################
print(df)
###### drop duplicates, create new column named discount
df = df.drop_duplicates(subset = ['StockCode','Quantity','CustomerID'])
print(df)
df["discount"] = 1 #creates a new row named discount
################################

row_count = 1;
for i in df.index:

    dis_val= discount(float(code_maxp[df["StockCode"][i]]),float(df["UnitPrice"][i]))
    df.at[i,"discount"] = int(dis_val)
    print(f"{row_count} / {len(df.index)}")
    row_count+=1



print(df)
### Use label encoding for StockCode and CustomerID
le = LabelEncoder()
df["StockCode"]  = le.fit_transform(df.StockCode.values)
df["CustomerID"]  = le.fit_transform(df.CustomerID.values)
#############################

df.to_csv("database.csv",header = True,index = False) #Contains the Unit Price. 

df = df.drop("UnitPrice",axis = 1)
df.to_csv("processed.csv",header = True,index = False)
