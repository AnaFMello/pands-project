## Analysis.py
## Author: Ana Figueiro

## Importing librariers to be able to use  the functions and methods they provide to perform data analysis and visualization tasks.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

## Loading the dataset: The first step is to load the iris dataset using pandas' read_csv() function. 
## The dataset is stored in a CSV file, and the read_csv() function is used to read the file and create a pandas DataFrame object called iris. 
## The sep parameter specifies the delimiter used in the CSV file, and names parameter is used to assign meaningful names to each column of the dataset.
iris = pd.read_csv('iris.data', sep=',', names=['sepal.length', 'sepal.width', 'petal.length', 'petal.width', 'iris-species'])

## Generating a summary of the data: The describe() function is used to generate a summary of each variable in the iris dataset. 
# The T function is used to transpose the summary table so that it is easier to read. The summary is then saved to a text file using Python's open() function in write mode ('w').
summary = iris.describe().T
with open('summary.txt', 'w') as f:
    f.write(str(summary))

## Creating histograms: A for loop is used to create a histogram of each variable in the iris dataset. 
# The hist() function is used to generate the histograms, and the resulting plots are saved to PNG files using the savefig() function.
for col in iris.columns[:-1]:
    plt.figure()
    iris.hist(column=col, bins=10, grid=False, edgecolor='black')
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.savefig(f'{col}_histogram.png', dpi=300)


## Preparing the data for analysis: The iris dataset is further prepared for analysis by creating a new 
# DataFrame called iris2 that contains the species column split into two separate columns, and then renamed to species. The iris and iris2 
# DataFrames are then concatenated using the concat() function, and the resulting DataFrame is assigned back to iris. 
# The iris-species column is dropped from the iris DataFrame.
iris2 = iris['iris-species'].str.split('-', n=1, expand=True)
iris2 = iris2.drop(columns=0)
iris2 = iris2.rename(columns={1: "species"})
iris = pd.concat([iris, iris2], axis=1)
iris = iris.drop(columns='iris-species')
iris.head()
iris.info()

## Generating a scatter plot: A scatter plot of petal width vs. length is generated using the scatterplot() 
# function from the seaborn library. The resulting plot is saved to a PNG file.
plt.figure(figsize=(8,6))
sns.scatterplot(data=iris, x='petal.length', y='petal.width', hue='species')
plt.title('Petal Width vs Length')
plt.xlabel('Width')
plt.ylabel('Length')
plt.show()

## Generating summary statistics for the setosa species: The minimum and maximum values for each 
# variable in the iris dataset for the setosa species are computed using the min() and max() functions, 
# and the resulting DataFrames are concatenated using the concat() function. The resulting DataFrame is printed to the console.
setosa_min = pd.DataFrame(iris[iris.species == 'setosa'].min(), columns=['minimum'])[0:4]
setosa_max = pd.DataFrame(iris[iris.species == 'setosa'].max(), columns=['maximum'])[0:4]
pd.concat([setosa_min, setosa_max], axis=1)


## Generating a histogram for each variable in the iris dataset: Using `iris.hist()`. The `figsize` parameter sets the size of the figure, 
# and `edgecolor` and `linewidth` parameters set the color and width of the borders for each histogram bar, it will result in histograms are displayed using `plt.show()`.
iris.hist(figsize=(12,6), edgecolor='black', linewidth=0.3)
plt.show()


## Creating a grid of scatter plots: Using seaborn's pairplot() function, showing the relationship between each pair of variables in the iris dataframe. 
# It colors each point based on the 'species' column, and displays the plot.
sns.pairplot(iris, hue= 'species');

## This code creates four violin plots using the Seaborn library `sns.violinplot()`. 
# Each plot displays a different variable (`petal.length`, `petal.width`, `sepal.length`, and `sepal.width`) on the y-axis, and the species of iris on the x-axis. 
# The resulting violin plots are displayed using `plt.show()`.
plt.figure(figsize=(10,8))
plt.subplot(2,2,1)
sns.violinplot(x='species', y='petal.length', data=iris)
plt.subplot(2,2,2)
sns.violinplot(x='species', y='petal.width', data=iris)
plt.subplot(2,2,3)
sns.violinplot(x='species', y='sepal.length', data=iris)
plt.subplot(2,2,4)
sns.violinplot(x='species', y='sepal.width', data=iris)
plt.show()

## This code creates a scatterplot matrix using the Seaborn library `sns.pairplot()`. 
# The `hue` parameter is set to 'species', which colors the scatterplot points by the species of iris being represented. 
# The resulting scatterplot matrix is saved as a PNG file named 'scatter_plot.png' using `plt.savefig()`, and is also displayed using `plt.show()`.
sns.pairplot(iris, hue='species')
plt.savefig('scatter_plot.png', dpi=300)
plt.show()

