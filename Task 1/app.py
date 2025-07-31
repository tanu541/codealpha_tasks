from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np
import joblib

app = Flask(__name__, static_folder='static')
CORS(app)

# Load the trained model
model = joblib.load("best_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)

        # Parse inputs
        sl = float(data['sepal_length'])
        sw = float(data['sepal_width'])
        pl = float(data['petal_length'])
        pw = float(data['petal_width'])

        features = np.array([[sl, sw, pl, pw]])
        prediction = model.predict(features)[0]

        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({'error': str(e)}), 500

# Optional: To serve image files if needed directly
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True, port=5500)