# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 01:50:25 2020

@author: ASUS
"""
# importer ttes les librai utilisées
from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np


def predict_loan(model, df):
    
    predictions_data = predict_model(estimator = model, data = df)
    
    return predictions_data['Label'][0]
    
model = load_model('Logis_Reg_model')


st.title('Immo Classifier Web App')

Gender = st.sidebar.slider(label = 'Gender, M=0, F=1 ', min_value = 0,
                          max_value = 1,
                          step = 1)

Married = st.sidebar.slider(label = 'Married, No=0, Yes=1 ', min_value = 0,
                          max_value = 1,
                          step = 1)   

Dependents = st.sidebar.slider(label = 'Dependents', min_value = 0, 
                            max_value = 3,
                            step=1)


Education = st.sidebar.slider(label = 'Education, Graduate=0, Not Graduate=1 ', min_value = 0,
                          max_value = 1,
                          step = 1)

Self_Employed = st.sidebar.slider(label = 'Self Employed, No=0, Yes=1 ', min_value = 0,
                          max_value = 1,
                          step = 1)

ApplicantIncome = st.sidebar.slider(label = 'Applicant Income', min_value = 150, 
                            max_value = 81000, step = 100)

CoapplicantIncome = st.sidebar.slider(label = 'Coapplicant Income', min_value = 0,
                          max_value = 41667,
                          step = 100)

LoanAmount = st.sidebar.slider(label = 'Loan Amount', min_value = 9,
                          max_value = 700,
                          step = 10)

Loan_Amount_Term = st.sidebar.slider(label = 'Loan Amount Term ', min_value = 12,
                          max_value = 480,
                          step = 1)

Credit_History = st.sidebar.slider(label = 'Credit History, No=0, Yes=1 ', min_value = 0,
                          max_value = 1,
                          step = 1)

Property_Area = st.sidebar.slider(label = 'Property Area', min_value = 0,
                          max_value = 2,
                          step = 1)
# to create feature
features = {'Gender': Gender,
            'Married': Married,  'Dependents' : Dependents, 'Education' : Education, 'Self_Employed' : Self_Employed, 'ApplicantIncome': ApplicantIncome, 'CoapplicantIncome': CoapplicantIncome,
            'LoanAmount': LoanAmount, 'Loan_Amount_Term': Loan_Amount_Term, 'Credit_History' : Credit_History, 'Property_Area': Property_Area,
            }

features_df  = pd.DataFrame([features])

#st.table(features_df)  

if st.button('Predict'):
    
    prediction = predict_loan(model, features_df)
    st.table(features_df)  
    st.write(' Based on feature values '+ str(prediction))
