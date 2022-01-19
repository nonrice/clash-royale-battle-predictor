from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras

model = keras.models.load_model("../models/{}".format(input("Saved model name? ")))

pred = model.predict("thing") 