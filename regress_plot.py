#! /usr/bin/env python3

"A script to perform linear regressions and to plot them"

import pandas as pd
dataframe = pd.read_csv("iris.csv")
type(dataframe)




print(dataframe)



quit()

#"""
#Returns a dataframe per Iris species
#"""

#versicolor = dataframe[dataframe.species == "Iris_versicolor"]

#import matplotlib.pyplot as plt
#from scipy import stats

#"""
#Returns a linear regression plot.

#Parameters
#----------
#Species : str
#Petal_length : float
#The length of the petals in cm
#Sepal_length : float
#The length of the sepal.

#Returns
#-------
#plot
#The linear regression between petals and sepals  of 3 different species

#"""
#if __name__ == '__main__':
#     if (len(sys.argv) < 2) or (len(sys.argv) > 3):
#        message = (


#import matplotlib.pyplot as plt
#from scipy import stats
#dataframe = pd.read_csv("iris.csv")
#x = dataframe.petal_length_cm
#y = dataframe.sepal_length_cm
#regression = stats.linregress(x, y)
#slope = regression.slope
#intercept = regression.intercept
#plt.scatter(x, y, label = 'Data')
#plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
#plt.xlabel("Petal length (cm)")
#plt.ylabel("Sepal length (cm)")
#plt.legend()
#plt.savefig("petal_v_sepal_length_regress.png")
