# app.py

from flask import Flask, request, jsonify
import subprocess
import joblib

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get input features from the request
    input_data = request.json.get('input_data')

    # Load the trained model
    model = joblib.load("iris_model.rds")

    # Make predictions
    prediction = model.predict(input_data)

    # Return the prediction as JSON
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
