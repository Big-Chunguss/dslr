import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/dataset_train.csv", usecols=['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying'])

# print(df)
# Pearson correlation (linear)
corr = df.corr()

sns.pairplot(df)
plt.show()


df2 = pd.read_csv("data/dataset_train.csv", usecols=['Astronomy', 'Defense Against the Dark Arts'])
corr = df2.corr()

sns.pairplot(df2)
plt.show()
