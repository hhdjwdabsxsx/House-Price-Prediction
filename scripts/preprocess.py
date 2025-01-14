import pandas as pd

def clean_data(data):
    # Drop irrelevant columns (e.g., ID, date)
    data = data.drop(['id', 'date'], axis=1)

    # Handle outliers
    data = data[data['bedrooms']<30]

    return data

def preprocess_data(data_path):
    data = pd.read_csv(data_path)
    data = clean_data(data)
    return data

if __name__ == "__main__":
    # Example usage
    data_path = "data/house_data.csv"
    preprocess_data = preprocess_data(data_path)
    print("Data preprocessing completed")