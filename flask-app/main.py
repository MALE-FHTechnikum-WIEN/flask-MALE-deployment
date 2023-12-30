import subprocess
from flask import Flask, request, jsonify, render_template

from model import run_model

app = Flask(__name__)

@app.route('/predict/<value>', methods=['GET'])
def predict(value):

    prediction = run_model(value)
    return jsonify({'Prediction': prediction})


@app.route('/info', methods=['GET'])
def info():
    # Debugging information
    return jsonify({'This app was created by:': ['Ernesto', 'Baptiste Gigachad']})

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET': #When a 'GET' request is pushed, the code below will be executed
        return render_template('index.html')

    if request.method == 'POST': #When a 'POST' request is pushed, the code below will be executed

        value = request.form.get('prediction', '')

        prediction = run_model(value)
        return render_template('index.html', response=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
