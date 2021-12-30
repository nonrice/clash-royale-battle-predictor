import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics
import tqdm
from matplotlib import pyplot as plt

battles_df = pd.read_csv("../data/data.csv").sample(frac=1)
X = battles_df.iloc[:,1:213]
y = battles_df.iloc[:,213]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = svm.SVC()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_train)
print("Accuracy:",metrics.accuracy_score(y_train, y_pred))

y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))