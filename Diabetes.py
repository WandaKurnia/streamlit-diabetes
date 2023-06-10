import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('Diabates.sav', 'rb'))

st.title(' Prediksi Penyakit Diabetes')

gender = st.number_input('GENDER')
age  = st.number_input('AGE')
hypertension = st.number_input('HYPERTENSI')
heart_disease = st.number_input('HEART DISEASE')
smoking = st.number_input('SMOKING')
bmi = st.number_input('BMI')
HbA1c_level = st.number_input('HbA1c_level')
blood_glucosa_level = st.number_input('BLOOD GLUCOSA')

Diabetes_diagnosis = ''

if st.button ('Prediksi Penyakit Diabetes'):
    Diabetes_prediction = model.predict([[gender, age, hypertension, heart_disease, smoking, bmi, HbA1c_level, blood_glucosa_level]])

    if (Diabetes_prediction[0]==1):
        Diabetes_diagnosis = 'mengidap'
    else:
        Diabetes_diagnosis = 'tidak mengidap'
    

st.success(Diabetes_diagnosis)
st.text('Wanda Kurnia WIdi - 201351135 - Malam A')

