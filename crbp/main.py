import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import joblib
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.regularizers import L1
from tensorflow.keras.optimizers import Adam
import os
from tensorflow.keras.callbacks import EarlyStopping
from tqdm.keras import TqdmCallback
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix

def enc_row(row_ord=tuple):
    row_enc = [0] * 215 
    for c in range(1, 17):
        if row_ord[c] > 211: print(row_ord[c])
        row_enc[row_ord[c]] = 1
    row_enc[212] = row_ord[17]
    row_enc[213] = row_ord[18]
    row_enc[214] = row_ord[19]
    
    return row_enc

df = pd.read_csv("../data/data_ord.csv").iloc[:,1:]

for c in range(1, 9):
    df["p2card{}".format(c)] = df["p2card{}".format(c)] + 106

cardlist = pd.read_csv("../data/cardlist.csv").iloc[:,1:]
cards = cardlist["card"]
columns = []
for i in range(1, 3):
    for card in cards:
        columns.append(card + str(i))
        
columns.append("trophies1")
columns.append("trophies2")
columns.append("outcome")

rows = []
for row in df.itertuples():
    rows.append(enc_row(row))
    
df_enc = pd.DataFrame(data=rows, columns=columns)

X = df_enc.iloc[:,0:214]
y = df_enc.iloc[:,214]

scaler = MinMaxScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1"

model = Sequential()
model.add(Dense(144, input_dim=214, activation="relu", kernel_regularizer=L1(0.0001), kernel_initializer="he_uniform"))
model.add(Dense(72, activation="relu", kernel_regularizer=L1(0.0001), kernel_initializer="he_uniform"))
model.add(Dense(36, activation="relu", kernel_regularizer=L1(0.0001), kernel_initializer="he_uniform"))
model.add(Dense(36, activation="relu", kernel_regularizer=L1(0.0001), kernel_initializer="he_uniform"))
model.add(Dense(36, activation="relu", kernel_regularizer=L1(0.0001), kernel_initializer="he_uniform"))
model.add(Dense(36, activation="relu", kernel_regularizer=L1(0.0001), kernel_initializer="he_uniform"))
model.add(Dense(1, activation="sigmoid", kernel_regularizer=L1(0.0001)))
model.summary()

model.compile(
    optimizer=Adam(learning_rate=0.0025),
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

epochs_hist = model.fit(
    X_train,
    y_train,
    shuffle=True,
    epochs=10,
    batch_size=196,
    verbose=0,
    validation_split=0.2,
    callbacks=[TqdmCallback(), EarlyStopping(monitor="val_loss", patience=10)]
)

if input("Show loss graph from training? (y/n) ") == "y":
    print("Generating graph...")
    plt.figure(dpi=100)
    plt.plot(epochs_hist.history['loss'], label="Training Loss")
    plt.plot(epochs_hist.history['val_loss'], label="Validation Loss")
    print("Close the graph window to continue the program.")
    plt.show()

print("Evaluating model on new data...")
y_pred = model.predict(X_test) 
y_pred = [1 if x >= 0.5 else 0 for x in y_pred]

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print("True Negative:", tn)
print("False Positive:", fp)
print("False Negative:", fn)
print("True Positive:", tp)
print("Final Accuracy:", (tp+tn)/(tp+tn+fp+fn))

if input("Save model? (y/n)") == "y":
    model_dir = input("Model name? ")
    os.mkdir("../models/{}".format(model_dir))
    model.save("../models/{}/model.h5".format(model_dir))
    joblib.dump(scaler, "../models/{}/scaler.save".format(model_dir)) 
    print("Model saved at directory {} in ../models/".format(model_dir))
