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

cards = pd.read_csv("data/cardlist.csv")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=109)

fs = SelectKBest(score_func=chi2, k=150)
fs.fit(X_train, y_train)

for i in range(len(fs.scores_)):
    print(str(cards.iloc[i][2]) + ": " + str(fs.scores_[i]))

X_train_fs = fs.transform(X_train)
X_test_fs = fs.transform(X_test)

model = Sequential()

model.add(Dense(96, activation="relu"))
model.add(Dropout(0.3))

model.add(Dense(96, activation="relu"))
model.add(Dropout(0.3))

model.add(Dense(96, activation="relu"))
model.add(Dropout(0.3))

model.add(Dense(1, activation="sigmoid"))
model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.SGD(learning_rate=0.001),
              metrics=['accuracy'])
history = model.fit(X_train_fs, y_train, batch_size=32, epochs=1000, verbose=0, validation_split=0.2, callbacks=[TqdmCallback(verbose=0)])

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])

plt.show()