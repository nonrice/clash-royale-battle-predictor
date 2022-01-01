Raw Neural Network:
Decks Only, Various configurations:
    RESULT: validation accuracy ~60%

SVM:
Decks Only, Chi2 SelectKBest 106:
    "kernel": RBF
    RESULT: validation accuracy 60.00936822999005%

XGBoost:
Decks Only, GridCV Optimized:
    "max_depth": 7,
    "min_child_weight": 12,
    "eta": 0.2,
    "subsample": 1,
    "colsample_bytree": 0.92,
    "objective": "binary:logistic"
    RESULT: validation accuracy 61.0876%