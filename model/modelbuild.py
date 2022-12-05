#Python Program which trains the model 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor
import pickle

#Modifying the dataset 
df = pd.read_csv("processed.csv")
X = df.iloc[:,:-1].values
y = df.iloc[:,3].values

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2,random_state = 10)


#Fitting multiple linear regression to the training set
regressor = DecisionTreeRegressor(random_state = 100)
r = regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)
score = r2_score(y_test,y_pred)*100
print(f"Model accuracy Score = {score} %") 

#Saving the model
pickle.dump(regressor,open("model.pkl","wb"))


