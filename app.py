from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

try:
    with open('car_model.pkl', 'rb') as f:
        data = pickle.load(f)
except EOFError:
    print("The file is empty or corrupted.")

@app.route('/predict', methods=['POST'])
def predict():
    
    data = request.json

    # Extracting the input data from the incoming JSON request
    car = data['Car']
    model_name = data['Model']
    volume = data['Volume']
    weight = data['Weight']
    co2 = data['CO2']

    # Prepare the feature vector for prediction
    feature_vector = [[volume, weight, co2]]

    # Making the prediction
    prediction = model.predict(feature_vector)

    # Return the prediction as a JSON response
    return jsonify({'predicted_price': prediction[0]})


@app.route('/')
def home_page():
    return render_template("index.html")  # Render the HTML file

if __name__ == "__main__":
    app.run(debug=True, port=8000)  # Run the app on port 8000
