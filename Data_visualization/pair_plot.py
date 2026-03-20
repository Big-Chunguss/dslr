import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys

if len(sys.argv) != 2:
    print("You need a single file path")
    exit(1)
file = pd.read_csv(sys.argv[1])
col_to_plot = ['Hogwarts House','Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 
                'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 
                'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']
col_to_plot2 = ['Hogwarts House','Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts']
print(file)
sns.pairplot(file[col_to_plot], hue='Hogwarts House')
plt.savefig("pair_plot.png")
plt.show()