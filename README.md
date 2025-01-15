# **House Price Prediction Web Application**

## **Overview**
This project is a Flask-based web application that predicts house prices based on input features using a machine learning model. Users can input various features of a house (e.g., number of bedrooms, bathrooms, size in square feet, and location), and the application predicts the house price using a trained machine learning model.

---

## **Assignment Objective**
Develop a Flask-based web application for predicting house prices using a machine learning model. The application:
1. Accepts input features such as the number of bedrooms, bathrooms, size in square feet, and location.
2. Predicts house prices using a machine learning model.
3. Provides a simple and user-friendly interface for interaction.

---

## **Features**
1. **Machine Learning Model Implementation**:
   - A Random Forest Regressor is trained on a housing dataset.
   - The model predicts house prices based on input features.

2. **Flask Web Application**:
   - User-friendly web interface.
   - Input form for entering house features.
   - Displays the predicted house price.

3. **Customizable and Extendable**:
   - Easily replaceable datasets and models.
   - Responsive design for seamless interaction on any device.

---

## **Technologies Used**
- **Backend**:
  - Flask (Python web framework)
  - Scikit-learn (for machine learning)
  - Joblib (for model serialization)
- **Frontend**:
  - HTML5
  - CSS3

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-repository/house-price-prediction.git
cd house-price-prediction
```
### **2. Create a Virtual Environent**
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
```
### **3. Install Dependencies**
Install the required Python packages:
```bash
pip install -r requirements.txt
```
### **4. Train the Model**
Train the machine learning model using the provided dataset:
```bash
python scripts/train_model.py
```
### **5. Run the Flask Application**
Start the Flask web server:
```bash
python app/app.py
```
The application will be available at http://127.0.0.1:5000/.

---

## **Usage**
1. Navigate to http://127.0.0.1:5000/ in your browser.
2. Enter the details of the house, including the number of bedrooms, bathrooms, size, and location.
3. Click the "Predict" button.
4. The predicted house price will be displayed.

---

## **Project Structure**
```bash
house_price_prediction/
├── app/
│   ├── app.py                        # Flask application
│   ├── static/
│   │   └── css/
│   │       └── style.css             # CSS file for styling
│   └── templates/
│       └── index.html                # HTML file for the web interface
├── data/
│   └── house_data.csv                # Dataset used for training the model
├── models/
│   └── house_price_model.pkl         # Trained machine learning model
├── scripts/
│   ├── preprocess.py                 # Data preprocessing script
│   ├── train_model.py                # Model training script
│   └── predict.py                    # Prediction script
├── requirements.txt                  # Python dependencies
└── README.md                         # Project documentation
```
## **License**
This project is licensed under the MIT License

