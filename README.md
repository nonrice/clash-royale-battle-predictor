# Clash Royale Battle Predictor
Neural network trained to predict the outcome of Clash Royale battles.

## Process
Top ladder battles are accessed through the [Clash Royale API](https://developer.clashroyale.com/#/). The cards in each player's decks and the outcome of each battle are encoded through one-hot encoding, creating roughly 200 features. Several thousand samples are created and then fed into a classifier, which is trained to recognize the impact each player's deck configuration impacts their win/loss chances against another player's configuration.

## Progress
- Updated training data to contain a larger list of Clash Royale ladder battles (3/4ths of 1 million)
- [Started configuring and training neural networks.](https://github.com/nonrice/clash-royale-battle-predictor/blob/main/logs.md)

#### Want to download the data? Visit and download `data/data.csv` from this repo.
- The first 106 cells describe **Player A's Deck.** The second 106 cells describe **Player B's Deck.** These sections are the result of One-Hot-Encoding. Encoding table can be found at `data/cardlist.csv`
- The next two columns describe the player's **trophy counts.**
- The final columns describe the **outcome of the battle.** `1` is displayed if Player A wins. Otherwise, `0`

## Used Packages
```
pandas 1.3.5
scikit-learn 1.0.2
tensorflow 2.7.0
matplotlib 3.5.1
tqdm 4.62.3
requests 2.26.0
```
