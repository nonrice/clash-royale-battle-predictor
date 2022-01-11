# Clash Royale Battle Predictor
Neural network trained to predict the outcome of Clash Royale battles.

## Details
- Takes in each player's deck and trophy counts. Returns the predicted outcome of their battle.
- Includes a data grabber `/crbp/data_grabber.py` to compile massive lists of battles (training data) through the [Clash Royale API](https://developer.clashroyale.com)
- Want to see other experiences with the same dataset? [Visit the Kaggle page here.](https://www.kaggle.com/nonrice/clash-royale-battles-upper-ladder-december-2021)

## How to Use
Download the code and unzip it. All Python scripts are located in the `/crbp` folder.
- `main.py` and `main.ipynb` both fully go through the training process. `main.ipynb` contains extra annotations.
- `data_grabber.py` collects training data by iterating through player battle logs in a list of Clash Royale clans. Criteria, such as minimum clan score and player minimum trophy count can be specified. Output is saved at `/data/data_ord.csv`, and `/data/cardlist.csv` provides a key to translate card numbers into their names.

## Required Packages
```
* - Required only for the data grabber
** - Required only for training
*** - Required for both

Name         Ver.   Req.
pandas       1.3.5  ***
scikit-learn 1.0.2  **
tensorflow   2.7.0  **
matplotlib   3.5.1  **
tqdm         4.62.3 ***
requests     2.26.0 *
```
