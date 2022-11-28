import pandas as pd

def discount(mrp,unit_price):
    return ((mrp-unit_price)/(mrp))*100

def mrp(max_unit_price):
    return max_unit_price*1 #can be changed later

df = pd.read_csv("data.csv",encoding = "ISO-8859-1")
df = df.dropna() #drop all Rows with any NaN value

df = df[df.Quantity>0] #Remove Items with a negative Quantity value
df = df[df.UnitPrice>0] #Remove items with Unit price <= zero (Free items)

df = df.drop('InvoiceNo',axis = 1) #remove un
df = df.drop('InvoiceDate',axis = 1)
df = df.drop('Country',axis = 1)
df = df.drop('Description',axis = 1)

### Data preprocessing part over.
### New Column addition: Discount

df["discount"] = 1 #creates a new row named discount
stock_codes = list(df.StockCode.unique())
code_maxp = dict()

for stock in stock_codes:
    code_maxp[stock] = mrp(max(df[df.StockCode == stock].UnitPrice.unique()))

for i in df.index:

    dis_val= discount(float(code_maxp[df["StockCode"][i]]),float(df["UnitPrice"][i]))
    df.at[i,"discount"] = dis_val
    print(df["discount"][i])



print(df)

df.to_csv("processed.csv",header = True,index = False)
