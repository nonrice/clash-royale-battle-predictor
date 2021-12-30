import pandas as pd
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from matplotlib import pyplot as plt
from tqdm.keras import TqdmCallback
from sklearn.model_selection import train_test_split

battles_df = pd.read_csv("data/data.csv").sample(frac=1)
X = battles_df.iloc[:,1:213]
y = battles_df.iloc[:,213]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = Sequential()

model.add(Dense(144, activation="sigmoid"))

model.add(Dense(144, activation="sigmoid"))

model.add(Dense(1, activation="sigmoid"))
model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.SGD(learning_rate=0.001),
              metrics=['accuracy'])
history = model.fit(X_train, y_train, batch_size=64, epochs=500, verbose=0, validation_split=0.3, callbacks=[TqdmCallback(verbose=0)])

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])

plt.show()