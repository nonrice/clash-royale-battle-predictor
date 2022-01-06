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
from sklearn.metrics import confusion_matrix

battles_df = pd.read_csv("../data/data.csv")

outliers = [] 

for i, row in battles_df.iterrows():
    diff = abs(row[213] - row[214])
    if diff > 1000:
        outliers.append(i)

battles_df = battles_df.drop(battles_df.index[outliers])   

X = battles_df.iloc[:,1:215]
y = battles_df.iloc[:,215]

scaler = MinMaxScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = Sequential()
model.add(Dense(144, input_dim=214, activation="relu", kernel_regularizer=L1(0.0001), kernel_initializer="he_uniform"))
model.add(Dense(144, activation="relu", kernel_regularizer=L1(0.0001), kernel_initializer="he_uniform"))
model.add(Dense(1, activation="sigmoid", kernel_regularizer=L1(0.0001)))
model.summary()

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.00025),
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
epochs_hist = model.fit(
    X_train,
    y_train,
    shuffle=True,
    epochs=512,
    batch_size=128,
    verbose=0,
    validation_split=0.2,
    callbacks=[TqdmCallback(), EarlyStopping(monitor="val_loss", patience=10)]
)

plt.plot(epochs_hist.history['loss'])
plt.plot(epochs_hist.history['val_loss'])
plt.show()


y_pred = model.predict(X_test) 
y_pred = [1 if x >= 0.5 else 0 for x in y_pred]

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print("True Negative: ", str(tn))
print("False Positive: ", str(fp))
print("False Negative: ", str(fn))
print("True Positive: ", str(tp))
print("Accuracy", str((tp+tn)/(tp+tn+fp+fn)))

if input("Save model? (y/n)") == "y":
    model.save("../models/trial2.h5")
