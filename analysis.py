## This program is able to:
## 1. Outputs a summary of each variable to a single text file,
## 2. Saves a histogram of each variable to png files, and
## 3. Outputs a scatter plot of each pair of variables.
## 4. Performs any other analysis you think is appropriate


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset from the CSV file into a DataFrame
df = pd.read_csv("iris.data")

# Output a summary of each variable to a text file
with open("variable_summaries.txt", "w") as file:
    file.write(str(df.describe()))

# Save a histogram of each variable to PNG files
for column in df.columns[:-1]:
    plt.figure()
    sns.histplot(data=df, x=column)
    plt.savefig(f"{column}_histogram.png")

# Output a scatter plot of each pair of variables
##sns.pairplot(df, hue="species")
##plt.savefig("scatter_plots.png")
