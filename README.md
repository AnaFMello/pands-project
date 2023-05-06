# pands-project
Author: Ana Mello

Summary Of The Fisher's Iris Dataset
The Iris flower dataset is a well-known multivariate dataset that was designed by British statistician and geneticist Ronald Aylmer Fisher as an example of discriminant analysis. It includes 150 cases (rows) and 5 variables (columns), which are Sepal.Length, Sepal.Width, Petal.Length, Petal.Width, and Species. The data comprises of three different species of the Iris flower: Iris setosa, Iris virginica, and Iris versicolor.
The primary objective of the discriminant analysis is to create a simple function that can classify a flower correctly based on the four measurements. This forms the foundation of developing "predictors" to enhance accuracy in dataset records.
In 1935, an American botanist named Edgar Anderson gathered data on the three distinct Iris species from the Gaspé Peninsula in Québec province, eastern Canada. The specimens were collected on the same day, by the same person, and measured using the same instruments.
Ronald Fisher utilized Anderson's data in 1936 to determine whether linear regression could be used to maximize the ratio of the difference between the specific means to the standard deviations within species. As a result, the Iris flower dataset has gained immense recognition as the "Hello World" in Data Analysis.

Code Explanation:
(Step by step is explained in the code.)
The code in this file, analysis.py, performs several analyses on the Iris dataset (iris.data), which contains measurements of the length and width of petals and sepals of three different species of Iris flowers.
The first part of the code reads in the Iris dataset using pandas, and then computes a summary of each variable using the describe() function. This summary is written to a text file called summary.txt.
The second part of the code creates a histogram for each variable and saves each histogram as a png file. These histograms are plotted using matplotlib.
Next, the code performs some data cleaning by splitting the "iris-species" column into two separate columns, one for the species name and one for the variety name. It then drops the original "iris-species" column and concatenates the new columns back onto the dataset.
The code then creates a scatter plot of petal length vs. petal width, colored by species using the seaborn library. It also creates a violin plot for each variable, showing the distribution of each variable by species.
Finally, the code creates a pairplot using seaborn to show the relationship between all pairs of variables, colored by species. This pairplot is saved as a png file.
Overall, this code provides a thorough analysis of the Iris dataset, including descriptive statistics, visualizations of the data, and data cleaning.

Reaserch:
https://pandas.pydata.org/docs/
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
https://www.kaggle.com/learn/overview
http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html
https://levelup.gitconnected.com/unveiling-the-mysteries-of-the-iris-dataset-a-comprehensive-analysis-and-machine-learning-f5c4f9dbcd6d
https://realpython.com/
https://numpy.org/doc/
https://docs.python.org/
https://www.datacamp.com/community/tutorials/seaborn-python-tutorial
https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda#:~:text=Data%20Insights%3A,-The%20pdf%20curve&text=If%20petal%20length%20%3C%202.1%2C%20then,then%20species%20is%20Iris%20Virginica
https://jupyter-notebook.readthedocs.io/en/stable/
https://www.kaggle.com/code/lalitharajesh/iris-dataset-exploratory-data-analysis
https://towardsdatascience.com/
https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
https://www.kaggle.com/code/zachgold/python-iris-data-visualizations
https://stackoverflow.com/
https://www.analyticsvidhya.com/blog/2021/06/guide-to-data-visualization-with-python-part-1/
https://archive.ics.uci.edu/ml/datasets/iris
https://seaborn.pydata.org/
https://matplotlib.org/stable/contents.html