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

melted = b.melt('n', var_name='cols', value_name='val')

sns.scatterplot(data=melted, x='n', y = 'val', s = 10)
sns.scatterplot(data=b, y='avg', x='n', color = 'RED')
plt.axhline(math.pi, color = "green")

plt.grid()
plt.show()