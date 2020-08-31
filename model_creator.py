# we will code our first machine learning algorithm for classification

from sklearn.datasets import load_iris

import pandas as pd

iris_dataset = load_iris()

# let's split our data into training and test

from sklearn.model_selection import train_test_split

X_train, X_test, y_train,y_test = train_test_split(iris_dataset['data'],iris_dataset['target'],random_state = 0,test_size = 0.2)


# import some magic
from sklearn.linear_model import LogisticRegression

# create an instance of a logistic regression

# logistic = 

logistic.fit(X_train, y_train)

import pickle

pkl_filename = 'logistic_model.pkl'

with open(pkl_filename, 'wb') as file:
	pickle.dump(logistic, file)
