#! /usr/bin/env python3


"Exercise5: Generate a script to perform linear regressions between structural flower whorls (petals vs  sepals) of three Iris species,& to graph this relationship using a scatterplot"


import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def iris_scatterplot():

    """
    Returns a linear regression scatterplot between petals and sepals of three Iris species.

    Parameters
    ----------
    Species : str
        Three Iris species (I_versicolor, I_setosa, I_virginica) 
    Petal_length : float
        The length of the petals in cm
    Sepal_length : float
        The length of the sepal.

    Requierements
    ---------
    CSV file that contains the flower information of three Iris species ("iris.csv")
    
    """

    dataframe = pd.read_csv("iris.csv")
    type(dataframe)
    setosa = dataframe[dataframe.species == "Iris_setosa"]
    versicolor = dataframe[dataframe.species == "Iris_versicolor"]
    virginica = dataframe[dataframe.species == "Iris_virginica"]


    x = setosa.petal_length_cm
    y = setosa.sepal_length_cm
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Iris setosa whrols flower length regression')
    plt.plot(x, slope * x + intercept, color = "red", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("Iris_setosa_regression.png")


    print("You got 3 scatterplots, one per Iris species")


    if __name__ == '__main__':
         iris_scatterplot()

