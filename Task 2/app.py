from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

# Load the trained model
with open("random_forest_regression_model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Extract numerical fields
        year = int(data['year'])
        present_price = float(data['present_price'])
        kms_driven = int(data['kms_driven'])
        owner = int(data['owner'])

        # Categorical encodings
        fuel = data['fuel_type']  # Petrol, Diesel, CNG
        seller = data['seller_type']  # Dealer, Individual
        transmission = data['transmission']  # Manual, Automatic

        # One-hot encoding manually (same as training)
        fuel_diesel = 1 if fuel == 'Diesel' else 0
        fuel_petrol = 1 if fuel == 'Petrol' else 0
        fuel_cng = 1 if fuel == 'CNG' else 0

        seller_dealer = 1 if seller == 'Dealer' else 0
        seller_individual = 1 if seller == 'Individual' else 0

        transmission_manual = 1 if transmission == 'Manual' else 0
        transmission_auto = 1 if transmission == 'Automatic' else 0

        # 11 input features
        features = np.array([[
            year, present_price, kms_driven, owner,
            fuel_diesel, fuel_petrol, fuel_cng,
            seller_dealer, seller_individual,
            transmission_manual, transmission_auto
        ]])

        prediction = model.predict(features)[0]
        return jsonify({'prediction': round(prediction, 2)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
