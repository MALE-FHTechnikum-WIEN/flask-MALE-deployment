from flask import Flask, request, jsonify
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
    return jsonify({'This app was created by:': ['Ernesto', 'Baptiste']})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
