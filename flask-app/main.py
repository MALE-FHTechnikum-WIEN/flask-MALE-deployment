from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)


@app.route('/predict/<value>', methods=['GET'])
def predict(value):

    print(value)

    # Return the prediction as JSON
    return jsonify({'prediction': 'xd'})


@app.route('/info', methods=['GET'])
def info():
    # Debugging information
    return jsonify({'This app was created by:': ['Ernesto', 'Baptiste Gigachad']})

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET': #When a 'GET' request is pushed, the code below will be executed
        return render_template('index.html')
    
    if request.method == 'POST': #When a 'POST' request is pushed, the code below will be executed
        #Prediction is the name we gave our input in the html form, the name has to be given to retrieve the correct data
        prediction = request.form.get('prediction', '')
        print(prediction)
        return render_template('index.html', response=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
