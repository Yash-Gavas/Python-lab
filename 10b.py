import pandas as pd
import matplotlib.pyplot as plt

def iris_dataset_operations():
    df = pd.read_csv('iris.csv')
    
    print("First 5 rows:")
    print(df.head())
    
    print("Last 5 rows:")
    print(df.tail())
    
    print("Dataset information:")
    print(df.info())
    
    print("Overview of each column:")
    print(df.describe())
    
    print("Plotting dataset:")
    df.plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm', title='Sepal Length vs Sepal Width')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    plt.show()

iris_dataset_operations()
