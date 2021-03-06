import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
import warnings

warnings.filterwarnings("ignore") # Remove redundant sklearn warning about column names for cosmetics :) 

card_list = pd.read_csv("../data/cardlist.csv")
card_dict = {} 
for row in card_list.itertuples():
    card_dict[row[3].lower()] = row[2]

model_dir = input("Saved model name? ")
model = keras.models.load_model("../models/{}/model.h5".format(model_dir))

x = []
for p in range(1, 3):
    for c in range(1, 9):
        card = input("Player {}'s card {}? ".format(p, c)).lower()
        while card not in card_dict or card_dict[card] + (p-1)*106 in x:
            print("Card '{}' does not exist, or is a duplicate.".format(card))
            card = input("Player {}'s card {}? ".format(p, c)).lower()

        x.append(card_dict[card] + (p-1)*106)

x.append(int(input("Player 1's Trophy Count? ")))
x.append(int(input("Player 2's Trophy Count? ")))

x_enc = [0] * 214 
for c in range(0, 16):
    x_enc[x[c]] = 1
x_enc[212] = x[16]
x_enc[213] = x[17]

scaler = joblib.load("../models/{}/scaler.save".format(model_dir))
x_enc = scaler.transform([x_enc])

pred = model.predict(x_enc)[0][0]
print("-----")
if pred >= 0.5:
    print("Prediction  ->  Player 1 Wins")
    print("Advantage   ->  + {} / 1.00000".format(round((pred-0.5)*2, 5)))
else:
    print("Prediction  ->  Player 2 Wins")
    print("Advantage   ->  {} / 1.00000".format(round((0.5-pred)*2, 5)))
print("-----")