import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tqdm.keras import TqdmCallback
from matplotlib import pyplot as plt

battles_df = pd.read_csv("../data/data.csv")
X = battles_df.iloc[:,1:213]
y = battles_df.iloc[:,213]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = Sequential()

model.add(Dense(units = 144, activation = "relu"))
model.add(Dropout(0.1))
model.add(Dense(units = 144, activation = "relu"))
model.add(Dropout(0.1))
model.add(Dense(units = 144, activation = "relu"))
model.add(Dropout(0.1))
model.add(Dense(units = 144, activation = "relu"))
model.add(Dropout(0.1))
model.add(Dense(units = 144, activation = "relu"))
model.add(Dropout(0.1))
model.add(Dense(units = 144, activation = "relu"))
model.add(Dropout(0.1))
model.add(Dense(units = 144, activation = "relu"))
model.add(Dropout(0.1))
model.add(Dense(units = 1, activation = "sigmoid"))

model.compile(loss = "binary_crossentropy", optimizer = tf.keras.optimizers.SGD(learning_rate = 0.00075), metrics = ["accuracy"])
history = model.fit(X_train, y_train, batch_size = 1024, epochs = 2000, shuffle = True, verbose=0, callbacks=[TqdmCallback(verbose=0)], validation_split=0.2)

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.show()