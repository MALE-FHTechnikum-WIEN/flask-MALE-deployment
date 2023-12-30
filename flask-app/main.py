from flask import Flask, request, jsonify, render_template
from model import run_model

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def info():
    return jsonify({'This app was created by:': ['Ernesto', 'Baptiste']})

@app.route('/', methods=['GET', 'POST'])
#This is basically a route to the "/" of our site (http://localhost:5000'/')
def index():
    if request.method == 'GET': 
    #When a 'GET' request is pushed, the code below will be executed

        return render_template('index.html')
        #We return the render_template() function to render the HTML template contained in our 'templates' directory
    
    if request.method == 'POST': 
        #When a 'POST' request is pushed, the code below will be executed
        
        sepal_length = request.form.get('sepal_length', '')
        sepal_width = request.form.get('sepal_width', '')
        #sepal_length and width are the names we gave our input in the html form, the name has to be given to retrieve the correct data
        
        answer = run_model(sepal_length, sepal_width)
        #The answer variable is the variable which is the return of our function run_model in which we passed our prediction variable defined earlier
            
        return render_template('index.html', response=answer)
        #In this redner_template we passed our variable answer which will be now called 'response' in our HTML template
    
@app.route('/predict/<value>', methods=['GET'])
#This is an equivalent API route : when we enter http://localhost:5000/predict/'our_value' it should return the prediction in an json API dictionary

def predict(value):

    prediction = run_model(value)
    return jsonify({'Prediction': prediction})


if __name__ == '__main__':
#For those who are not familiar with python or oriented-object, it's just the part of the code that execute everything
    app.run(host='0.0.0.0', debug=True)
