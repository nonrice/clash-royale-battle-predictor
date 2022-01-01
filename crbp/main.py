import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb


battles_df = pd.read_csv("../data/data.csv")
X = battles_df.iloc[:,1:213]
y = battles_df.iloc[:,213]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

params = {
    "max_depth":7,
    "min_child_weight": 12,
    "eta": 0.2,
    "subsample": 1,
    "colsample_bytree": 0.92,
    "objective": "binary:logistic"
}

params['eval_metric'] = "error"
num_boost_round = 5000

model = xgb.train(
    params,
    dtrain,
    num_boost_round=num_boost_round,
    evals=[(dtest, "Test")],
    early_stopping_rounds=10
)

print("Best MAE: {} in {} rounds".format(model.best_score, model.best_iteration+1))