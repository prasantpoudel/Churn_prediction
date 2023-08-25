import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import pickle
from keras.models import load_model

def main():
    st.title("Customer Satisfaction Prediction")
    model= load_model('custom_ann.h5')
    st.markdown(
        """ 
   """
    )

    Age = st.number_input("Enter The Age(In years)",value=0)
    Subscription_Length_Months = st.number_input("Subscription Length Months(In Months)",value=0)
    Monthly_Bill = st.number_input("Monthly Bill",value=0)
    Total_Usage_GB	 = st.number_input("Total Usage (In GB)",value=0)
    gender = st.radio("Select your gender:", ("Male", "Female"))
    Gender_Male= 1 if gender == "Male" else 0
    Location= st.radio("Select your location:", ("Houston","Los Angeles","Miami","New York","Chicago"))
    Location_Houston= 1 if Location == "Houston" else 0
    Location_Miami= 1 if Location == "Miami" else 0
    Location_New_York= 1 if Location == "New York" else 0
    Location_Los_Angeles= 1 if Location == "Los Angeles" else 0
    Location_Chicago= 1 if Location == "Chicago" else 0


    if st.button("Predict"):
        
        features = [[Age,Subscription_Length_Months,Monthly_Bill,Total_Usage_GB,Gender_Male,Location_Houston,Location_Miami,Location_New_York,Location_Los_Angeles]]
        predict=model.predict(features)
        if predict[0][0] >= 0.5:
            value = "Churn"
        else:
            value = "Not Churn"
        st.write(value)
        st.write(predict[0][0])
if __name__ == "__main__":
    main()