# 🏡 House Price Prediction Project

This project predicts house prices in India based on various features of the house. It includes a Jupyter Notebook for model training and a Streamlit web application for demonstrating the model's predictions.

---

## 🚀 Live Demo

You can run the Streamlit app locally to see a live demo. The app provides a user-friendly interface to input house features and get a price prediction.

---

## ✨ Features

* **Interactive Price Prediction**: Users can input features like the number of bedrooms, bathrooms, living area, house condition, and the number of nearby schools to get a price prediction.
* **Machine Learning Model**: A Random Forest Regressor model is trained on the "House Price India" dataset.
* **User-Friendly Interface**: The Streamlit app is designed to be simple and intuitive.

---

## 📊 Dataset

The project uses the `House Price India.csv` dataset, which contains the following columns:

* `id`: A unique identifier for each house.
* `Date`: The date the house was sold.
* `number of bedrooms`: The number of bedrooms in the house.
* `number of bathrooms`: The number of bathrooms in the house.
* `living area`: The square footage of the living area.
* `lot area`: The square footage of the lot.
* `number of floors`: The number of floors in the house.
* `waterfront present`: A binary variable indicating if the house has a waterfront view.
* `number of views`: The number of times the house has been viewed.
* `condition of the house`: A rating of the house's condition.
* `grade of the house`: A rating of the house's grade.
* `Area of the house(excluding basement)`: The square footage of the house excluding the basement.
* `Area of the basement`: The square footage of the basement.
* `Built Year`: The year the house was built.
* `Renovation Year`: The year the house was renovated.
* `Postal Code`: The postal code of the house's location.
* `Lattitude`: The latitude of the house's location.
* `Longitude`: The longitude of the house's location.
* `living_area_renov`: The square footage of the living area after renovation.
* `lot_area_renov`: The square footage of the lot after renovation.
* `Number of schools nearby`: The number of schools in the vicinity.
* `Distance from the airport`: The distance from the nearest airport.
* `Price`: The price of the house.

---

## 💻 Installation

To run this project, you need to have Python installed. Follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/ayush-2323/House_Price_Predictor.git
    cd House_Price_Predictor
    ```
2.  **Create a `requirements.txt` file** with the following content:
    ```
    streamlit
    pandas
    scikit-learn
    joblib
    numpy
    ```
3.  **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

---

## 🏃‍♀️ Usage

1.  **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```
2.  Open your web browser and go to the local URL provided by Streamlit (usually `http://localhost:8501`).
3.  Enter the required features of the house in the input fields.
4.  Click the "Predict" button to see the estimated price.

---

## 🤖 Model

The prediction model is a `RandomForestRegressor` trained using `GridSearchCV` for hyperparameter tuning. The features used for training are:
* `number of bedrooms`
* `number of bathrooms`
* `living area`
* `condition of the house`
* `Number of schools nearby`

The trained model is saved in the `house_price_model.pkl` file.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** for data manipulation and analysis.
* **Scikit-learn** for building the machine learning model.
* **Streamlit** for creating the web application.
* **Jupyter Notebook** for model development and experimentation.

---

## 👨‍💻 Author

* **Ayush Kumar** 
