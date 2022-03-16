#! /usr/bin/env python3


"Exercise5: Generate a script to perform linear regressions between structural flower whorls (petals vs  sepals) of three Iris species"


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

    First step is to create new variables (objects) that contain the flower whorls information per each species
    We will get 3 new variables (objects)

    """

    dataframe = pd.read_csv("iris.csv")
    type(dataframe)

    setosa = dataframe[dataframe.species == "Iris_setosa"]
    versicolor = dataframe[dataframe.species == "Iris_versicolor"]
    virginica = dataframe[dataframe.species == "Iris_virginica"]

    """
    Once that the new variables where created, this script is going to cretea 3 scatterplots, one per scpecies

    """

    x = setosa.petal_length_cm
    y = setosa.sepal_length_cm
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'I.setosa whrols flower length regression')
    plt.plot(x, slope * x + intercept, color = "red", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("Iris_setosa_regression.png")
    plt.clf()
    print("You got 1 scatterplot")


    x = versicolor.petal_length_cm
    y = versicolor.sepal_length_cm
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'I.versicolor whrols flower length regression')
    plt.plot(x, slope * x + intercept, color = "green", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("Iris_versicolor_regression.png")
    plt.clf()
    print("You got 2 scatterplots")


    x = virginica.petal_length_cm
    y = virginica.sepal_length_cm
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'I.virginica whrols flower length regression')
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("Iris_virginica_regression.png")
    plt.clf()
    print("You got 3 scatterplots, one per Iris species")


if __name__ == '__main__':
    iris_scatterplot()

