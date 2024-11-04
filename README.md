# Clash Royale Battle Predictor
Neural network trained to predict the outcome of Clash Royale battles.

## Details
- Takes in each player's deck and trophy counts. Returns the predicted outcome of their battle.
- Includes a data grabber `/crbp/data_grabber.py` to compile massive lists of battles (training data) through the [Clash Royale API](https://developer.clashroyale.com)
- Scraped dataset has been uploaded: [Visit Kaggle page here.](https://www.kaggle.com/nonrice/clash-royale-battles-upper-ladder-december-2021)

![terminal demo](https://i.ibb.co/vBRKTJh/crbpterminaldemo.png)

## Predicting
1. Install libraries specified in `requirements.txt`
2. Run the file `predictor.py`
3. Use `final` for the model name. Models are stored as folders inside `/models`, the `final` model comes with the code.
4. Enter deck data and trophy counts. **Case does not matter, but you must use the real card names e.g. "The Log" instead of "Log".** 
5. The resulting prediction has an "advantage" value which ranges from 0 to 1. It describes just how much stronger the winning player will be.

## Contents
- `predictor.py` takes a trained model and runs user-given inputs through it.
- `main.py` is the full training process of the model. This file also allows saving of models. Models are saved as individual folders in the `/models` folder.
- `main.ipynb` is the full training process, but with detailed anotations. 
- `data_grabber.py` collects training data by iterating through player battle logs in a list of Clash Royale clans. Output is saved at `data/data_ord.csv`, and `data/cardlist.csv` provides a key to translate card numbers into their names.
