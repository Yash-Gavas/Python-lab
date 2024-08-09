import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('iris.csv')

# Visualize
data.plot()
plt.title('Dataset Visualization')
plt.show()
#Scatter plot
data.plot.scatter(x='sepal.length', y='sepal.width')
plt.title('Scatter Plot between Column1 and Column2')
plt.show()

# Colourfull scatter plot

categories =data['variety'].unique()
colors = plt.cm.rainbow(np.linspace(0, 1, len(categories)))

for i, category in enumerate(categories):
    subset =data[data['variety'] == category]
    plt.scatter(subset['sepal.length'], subset['sepal.width'], color=colors[i], label=category)

plt.xlabel('sepal.length')
plt.ylabel('sepal.width')
plt.title('Scatter Plot of A vs B with Different Colours')
plt.legend()
plt.show()


# Histogram
data['sepal.length'].plot.hist()
plt.title('Histogram of length of sepal and petal')
plt.xlabel('sepal.length')
plt.ylabel('petal.length')
plt.show()