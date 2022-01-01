import pandas as pd
from sklearn.manifold import TSNE
import seaborn as sns
from matplotlib import pyplot as plt

battles_df = pd.read_csv("../data/data.csv").iloc[:, 1:214]
model = TSNE(verbose=1, n_iter=20000, perplexity=42, learning_rate=20)

features = model.fit_transform(battles_df)
battles_df["x"] = features[:,0]
battles_df["y"] = features[:,1]
battles_df.to_csv("../data/data_tsne.csv")

plot = sns.scatterplot(x="x", y="y", data=battles_df, hue="212", s=2, edgecolor=None)
plot.set(title="t-SNE 2D, n_iter=20000")
plot.legend(title="Player 1 Win/Loss")
plt.show()