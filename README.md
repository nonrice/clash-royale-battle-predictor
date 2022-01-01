# Clash Royale Battle Predictor
By collecting battle data from top players, the goal is to train an artificial neural network to predict the outcome of any given card matchup.

## Process
Top ladder battles are accessed through the [Clash Royale API](https://developer.clashroyale.com/#/). The cards in each player's decks and the outcome of each battle are encoded through one-hot encoding, creating roughly 200 features. Several thousand samples are created and then fed into an artificial neural network, which is trained to recognize the impact each player's deck configuration impacts their win/loss chances against another player's configuration.

## Progress
```
ANN:
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
```

## Used Packages
```
pandas 1.3.5
scikit-learn 1.0.2
tensorflow 2.7.0
matplotlib 3.5.1
tqdm 4.62.3
requests 2.26.0
```
