# flask-lab
Template for Flask ML Lab

The objective of this lab is to create your own Flask app able to deliver predictions in the context of a supervised machine learning problem.

The dataset used is the classical Iris dataset.

In this lab you will have to modify:

model_creator: finsih the necessary functions and run this code in order to generate the trained model file

ml_model: this function will be called by the flask app to make a prediction. You need to load the model correctly and pass the appropriate parameters

app.py : this file runs the flask server. You must make sure the parameters returned from the html are appropriately stored and passed to the model function

DockerFile: you must adapt this file to create you docker image. Very similar to what was done in the class

first.html: no changes are required to this file. All the code is there ready to be rendered