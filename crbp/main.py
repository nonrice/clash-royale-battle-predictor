import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.regularizers import L1
from tqdm.keras import TqdmCallback
from matplotlib import pyplot as plt


battles_df = pd.read_csv("../data/data.csv").sample(frac=1)
X = battles_df.iloc[:,1:215]
y = battles_df.iloc[:,215]

outliers = []

for i, row in battles_df.iterrows():
    diff = abs(row[213] - row[214])
    if diff > 1000:
        outliers.append(i)

battles_df.drop(battles_df.index[outliers])    

scaler = MinMaxScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = Sequential()
model.add(Dense(144, input_dim=214, activation="relu", kernel_regularizer=L1(0.0001)))
model.add(Dense(144, activation="relu", kernel_regularizer=L1(0.0001)))
model.add(Dense(1, activation="sigmoid", kernel_regularizer=L1(0.0001)))
model.summary()

model.compile(
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.001),
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
epochs_hist = model.fit(
    X_train,
    y_train,
    epochs=256,
    batch_size=64,
    verbose=0,
    validation_split=0.2,
    callbacks=[TqdmCallback(), EarlyStopping(monitor="val_loss", patience=5)]
)

plt.plot(epochs_hist.history['loss'])
plt.plot(epochs_hist.history['val_loss'])
plt.show()