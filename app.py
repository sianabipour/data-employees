import streamlit as st
import joblib 
import numpy as np

st.set_page_config(page_title="Salary Prediction",page_icon=':earth_africa:')

st.title("Salary Prediction App")

st.divider()

st.write("With this app, you can make estimations for the salaries of employees")

years = st.number_input("Enter the years for company",value=1 , step=1 , min_value=0)
jobrate = st.number_input("Enter your Job Rate",value=3.5,step=0.5, min_value=0.0 )

X = [years,jobrate]

model = joblib.load('linearmodel.pkl')

st.divider()

predict = st.button("Press the button for salary prediction!")

st.divider()


if predict:
    
    st.balloons()
    X1 = np.array([X])
    prediction = model.predict(X1)[0]
    
    st.write(f"Salary prediction is {prediction:.2f}")
    
    
else:
    
    "Please press button for app to make prediction"