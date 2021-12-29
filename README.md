# Clash Royale Battle Predictor
By collecting battle data from top players, the goal is to train an artificial neural network to predict the outcome of any given card matchup.

## Process
Top ladder battles are accessed through the [Clash Royale API](https://developer.clashroyale.com/#/). The cards in each player's decks and the outcome of each battle are encoded through one-hot encoding, creating roughly 200 features. Several thousand samples are created and then fed into an artificial neural network, which is trained to recognize the impact each player's deck configuration impacts their win/loss chances against another player's configuration.

## Progress
Current results can accurately predict battle outcomes with up to 60% accuracy. There is a slight chance this could be the limit, knowing that games akin to these require much more than a good deck configuration. While this is the boring answer, I am hopeful that in time, we will see the exciting one.

## Used Packages
```
pandas 1.3.5
scikit-learn 1.0.2
tensorflow 2.7.0
matplotlib 3.5.1
tqdm 4.62.3
requests 2.26.0
```
