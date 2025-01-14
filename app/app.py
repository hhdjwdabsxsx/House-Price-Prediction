from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("models/house_price_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract input features from form
    features = [
        float(request.form['bedrooms']),
        float(request.form['bathrooms']),
        float(request.form['sqft_living']),
        float(request.form['sqft_lot']),
        float(request.form['floors']),
        int(request.form['waterfront']),
        int(request.form['view']),
        int(request.form['condition']),
        int(request.form['grade']),
        float(request.form['sqft_above']),
        float(request.form['sqft_basement']),
        int(request.form['yr_built']),
        int(request.form['yr_renovated']),
        int(request.form['zipcode']),
        float(request.form['lat']),
        float(request.form['long']),
        float(request.form['sqft_living15']),
        float(request.form['sqft_lot15']),
    ]
    
    # Predict the price
    prediction = model.predict([features])[0]
    return render_template('index.html', prediction=f"${prediction:,.2f}")

if __name__ == "__main__":
    app.run(debug=True)
