import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import math

#a1 = pd.read_csv("a_1.csv", header=0)
#print (a1.head())

#a2 =pd.read_csv("a_2.csv", header=0)
#print (a2.head())

#a3 = pd.read_csv("a_3.csv", header=0)
#print (a3.head())

b = pd.read_csv("b.csv", header=0)
#print (b.head())

bmelted = b.melt('n', var_name='cols', value_name='vals')

sns.scatterplot(data=bmelted, x='n', y = 'vals', s = 10)
sns.scatterplot(data=b, y='avg', x='n', c = 'red')
plt.axhline(math.pi, color = "green")

plt.grid()
plt.show()