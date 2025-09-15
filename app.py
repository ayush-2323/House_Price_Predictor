import streamlit as st
import joblib
import numpy as np

model = joblib.load("house_price_model.pkl")

st.title("House Price Predictor")

st.divider()

st.write("This app uses machine learning for predicting house price with given features of the house. For using this app you can enter the inputs from this UI and then use Predict button")

st.divider()

bedrooms = st.number_input("Number of Bedrooms", min_value=1, value=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, value=1)
living_area = st.number_input("Living Area (in sqft)", min_value=0, value=2000)
condition = st.number_input("Condition of the House (0-5)", min_value=0, value=3)
schools = st.number_input("Number of Schools Nearby", min_value=0, value=0)

st.divider()

x = [[bedrooms, bathrooms, living_area, condition, schools]]

predict_button = st.button("Predict")

if predict_button:

    st.spinner()

    x_array = np.array(x)

    prediction = model.predict(x_array)

    st.write(f"The predicted price of the house is ${prediction[0]:.2f}")

else:
    st.write("Please use Predict button after entering the values to get the price")







#Order of x ['number of bedrooms', 'number of bathrooms', 'living area',
           # 'condition of the house', 'Number of schools nearby']