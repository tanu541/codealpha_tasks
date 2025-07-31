# CodeAlpha Virtual Internship - Data Science Track

This repository contains two completed tasks submitted for the **CodeAlpha Data Science Virtual Internship Program**. Out of the four available options, I have completed the following:

1. Iris Flower Classification
2. Car Price Prediction

Both projects involve data preprocessing, model training, and building a user-friendly frontend integrated with a Flask-based backend for predictions.

##  Task 1: Iris Flower Classification

###  Problem Statement
Classify the species of iris flower based on 4 features:  
- Sepal Length  
- Sepal Width  
- Petal Length  
- Petal Width

###  Technologies Used
- Python (Scikit-learn, Pandas, NumPy)
- Flask
- HTML, CSS, JavaScript
- VS Code

###  ML Model
- Model: RandomForestClassifier
- Accuracy: ~96%
- Trained using `Iris` dataset from `sklearn.datasets`

 How It Works
1. User inputs the 4 flower measurements.
2. Frontend sends data to Flask backend (`/predict` endpoint).
3. Model returns the predicted class (Setosa, Versicolor, Virginica).
4. Web app displays the flower name and an image of the predicted species.
<img width="2880" height="1704" alt="Screenshot 2025-07-31 201551" src="https://github.com/user-attachments/assets/85e3ff47-26eb-44e4-bc3b-26af54908bf8" />
<img width="2880" height="1704" alt="Screenshot 2025-07-31 201438" src="https://github.com/user-attachments/assets/0902ebd6-6c5d-4240-b09a-6be439e9fe51" />
<img width="2880" height="1704" alt="Screenshot 2025-07-31 201346" src="https://github.com/user-attachments/assets/8332e095-bd2d-4443-bd2b-b1f1f50345a1" />

##  Task 2: Car Price Prediction

### Problem Statement
Predict the price of a used car based on various features such as:  
- Year  
- Present Price  
- Kms Driven  
- Fuel Type  
- Seller Type  
- Transmission  
- Owner
  
###  Technologies Used
- Python (Pandas, NumPy, Scikit-learn)
- Flask
- HTML, CSS, JavaScript
- VS Code

###  ML Model
- Model: RandomForestRegressor
- Metrics: R² Score ≈ 0.85
- Data Preprocessing: Encoding categorical variables, feature scaling

###  How It Works
1. User enters car details via the web interface.
2. Data is sent to the backend API.
3. Model processes input and returns predicted price.
4. Result is displayed dynamically on the webpage.
<img width="2292" height="1568" alt="Screenshot 2025-07-31 202057" src="https://github.com/user-attachments/assets/9cb69151-a241-4578-86da-9351701d051d" />
