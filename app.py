from flask import Flask, render_template, request
from ml_model import plant_classifier

app = Flask(__name__)
@app.route('/', methods = ['POST','GET'])

@app.route('/')

def index():
	if request.method == 'POST':

        # read from the fron end the correct variables
	   	#sepal_length =
	   	#sepal_width = 
	   	#petal_length = 
	   	#petal_width = 


        # call your ml model from
	   	result = spam_classifier(input_string)
	   	return render_template('first.html', text = result)

	else: 
		return render_template('first.html')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')