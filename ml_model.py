import pickle

def plant_classifier(sepal_length, sepal_width, petal_length, petal_width):

	# import the classifier pickle object 
	with open("something.pkl", 'rb') as file:
		model = pickle.load(file)

	# apply the .predict method to the input text and make this function return that result
	result = model.predict([sepal_length, sepal_width, petal_length, petal_width])
	return result


if __name__ == '__main__':


	# test it out here!
	print(plant_classifier(1,2,3,4))