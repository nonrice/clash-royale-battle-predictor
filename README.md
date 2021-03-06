# Clash Royale Battle Predictor
Neural network trained to predict the outcome of Clash Royale battles.

## Details
- Takes in each player's deck and trophy counts. Returns the predicted outcome of their battle.
- Includes a data grabber `/crbp/data_grabber.py` to compile massive lists of battles (training data) through the [Clash Royale API](https://developer.clashroyale.com)
- Want to see other experiences with the same dataset? [Visit the Kaggle page here.](https://www.kaggle.com/nonrice/clash-royale-battles-upper-ladder-december-2021)

![terminal demo](https://i.ibb.co/vBRKTJh/crbpterminaldemo.png)

## How to Use
1. Download the code and unzip it.
2. Navigate to the `crbp` folder inside the project contents
3. Run the file `predictor.py`
4. Use `final` for the model name. Models are stored as folders inside `/models`, the `final` model comes with the code.
5. Enter deck data and trophy counts. **Case does not matter, but you must use the real card names e.g. "The Log" instead of "Log".** 
6. The resulting prediction has an "advantage" value which ranges from 0 to 1. It describes just how much stronger the winning player will be.

## Contents
- `predictor.py` takes a trained model and runs user-given inputs through it.
- `main.py` is the full training process of the model. This file also allows saving of models. Models are saved as individual folders in the `/models` folder.
- `main.ipynb` is the full training process, but with detailed anotations. 
- `data_grabber.py` collects training data by iterating through player battle logs in a list of Clash Royale clans. Output is saved at `/data/data_ord.csv`, and `/data/cardlist.csv` provides a key to translate card numbers into their names.

[Made by @nonrice on Github.](https://github.com/nonrice)

# Dependencies
### Required Packages (Predictor)
```
Name         Ver.
pandas       1.3.5
joblib       1.1.0
scikit-learn 1.0.2
tensorflow   2.7.0
```

### Required Packages (Data Grabber/Training)
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
