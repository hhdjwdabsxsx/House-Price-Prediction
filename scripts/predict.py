import joblib
import numpy as np

def load_model(model_path):
    model = joblib.load(model_path)
    return model

def make_prediction(model, input_features):
    prediction = model.predict([input_features])
    return prediction[0]

if __name__ == "__main__":
    # Example input features (Replace with actual features)
    input_features = [3, 2.5, 2000, 5000, 2, 0, 0, 3, 7, 1800, 200, 1995, 0, 98052, 47.6396, -122.1281, 1900, 6000]

    # Load the model
    model_path = "models/house_price_model.pkl"
    model = load_model(model_path)

    # Make a prediction
    predicted_price = make_prediction(model, input_features)
    print(f"Predicted Price: ${predicted_price:.2f}")