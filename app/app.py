from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("models/house_price_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        try:
            # Get data from the form
            features = [
                float(request.form["bedrooms"]),
                float(request.form["sqft_living"]),
                float(request.form["bathrooms"]),
                float(request.form["sqft_lot"]),
                float(request.form["floors"]),
                float(request.form["waterfront"]),
                float(request.form["view"]),
                float(request.form["condition"]),
                float(request.form["grade"]),
                float(request.form["sqft_above"]),
                float(request.form["sqft_basement"]),
                float(request.form["yr_built"]),
                float(request.form["yr_renovated"]),
                float(request.form["zipcode"]),
                float(request.form["lat"]),
                float(request.form["long"]),
                float(request.form["sqft_living15"]),
                float(request.form["sqft_lot15"]),
            ]

            # Reshape features and predict
            features_array = np.array(features).reshape(1, -1)
            prediction = model.predict(features_array)[0]

            # Render the result in the same page
            return render_template("index.html", prediction_text=f"The predicted price is ${prediction:,.2f}")

        except Exception as e:
            # Handle errors
            return render_template("index.html", prediction_text="Error in processing: " + str(e))

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
