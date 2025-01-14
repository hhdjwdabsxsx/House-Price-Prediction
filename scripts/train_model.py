"""
train_model.py

This script preprocessed the housind data, trains a regression model, evaluates it, and saves the trained model.
"""

import joblib
from preprocess import preprocess_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def train_model(X_train, y_train):
    """
    Trains a Random Forest Regressor on the training data.

    Parameters:
    X_train (DataFrame): Training features.
    y_train (Series): Training target.

    Returns:
    RandomForestRegressor: The trained model.
    """
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def save_model(model, output_path):
    """
    Saves the trained model to a file.

    Parameters:
    model (RandomForestRegressor): The trained model.
    output_path (str): Path to save the model.
    """
    joblib.dump(model, output_path)
    print(f"Model save to {output_path}")

if __name__ == "__main__":
    # Load and preprocess data
    data_path = "data/house_data.csv"
    data = preprocess_data(data_path)

    # Split the features and target
    X = data.drop('price', axis=1)
    y = data['price']

    # Train_test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")

    # Save the model
    save_model(model, "models/house_price_model.pkl")

