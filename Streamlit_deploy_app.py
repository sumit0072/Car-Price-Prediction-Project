import numpy as np
import pandas as pd
import streamlit as st
import pickle

html_temp = """
<div style="background-color:tomato;padding:5px">
<h2 style="color:white;text-align:center;">Car Price Prediction using Machine Learning</h2>
</div><br>
"""
st.markdown(html_temp,unsafe_allow_html=True)


from PIL import Image
image = Image.open('Car_Price_Prediction.jpg')
st.image(image, width= 600)

st.write("""

### Made by ❤ Sumit Mohod
##

""")



Present_Price = st.text_input("Present market price of the Car (in Lakhs)", "10")

Kms_Driven = st.text_input("Kms driven by car", "20000")

owners = st.selectbox("Number of Previous Owners ?", ("0", "1", "3"))
if owners == '0':
    owners = 0
elif owners == '1':
    owners = 1
elif owners == '3':
    owners = 3
    
years_old = st.text_input("How old is the Car ? (in Years)", "3")

fuel_type = st.selectbox("Fuel type of Car", ("Diesel", "Petrol", "CNG"))
if fuel_type == 'Diesel':
    Fuel_type_Diesel = 1
    Fuel_type_Petrol = 0
    
elif fuel_type == 'Petrol':
    Fuel_type_Diesel = 0
    Fuel_type_Petrol = 1
    
elif fuel_type == 'CNG':
    Fuel_type_Diesel = 0
    Fuel_type_Petrol = 0
    
Individual = st.selectbox('Are you an Individual or Dealer ?', ("Individual", "Dealer"))
if Individual == "Individual":
    Seller_Type_Individual = 1
elif Individual == "Dealer":
    Seller_Type_Individual = 0
    
Transmission = st.selectbox("What kind of transmission does it have ?", ("Manual", "Automatic"))
if Transmission == 'Manual':
    Transmission_Manual = 1
else:
    Transmission_Manual = 0
    
if st.button("Predict"):
    pickle_in = open("random_forest_regression_model.pkl", "rb")
    rf_classifier_model = pickle.load(pickle_in)
    
    prediction = rf_classifier_model.predict([[Present_Price, Kms_Driven, owners, years_old, Fuel_type_Diesel, Fuel_type_Petrol, Seller_Type_Individual, Transmission_Manual]])
    output = round(prediction[0],2)
    
    st.write(f"""
    
    ### The  predicted selling price  for the car is : Rs. 
{output} lakhs
    
    """)
    
    