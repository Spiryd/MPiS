import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

a1 = pd.read_csv("a_1.csv", header=0)
#print (a1.head())

a2 =pd.read_csv("a_2.csv", header=0)
#print (a2.head())

a3 = pd.read_csv("a_3.csv", header=0)
#print (a3.head())

b = pd.read_csv("b.csv", header=0)
#print (b.head())

ys = map(str, list(range(1,51)))

sns.scatterplot(data = b, x = 'n' , y = 'avg')
plt.show()