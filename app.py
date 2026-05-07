

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and scaler
model = joblib.load('fraud_xgb_model.pkl')
scaler = joblib.load('fraud_scaler.pkl')

st.title("Banking Fraud Detection System")

st.write("Enter transaction details")

# Inputs
amount = st.number_input("Transaction Amount")

transaction_hour = st.slider(
    "Transaction Hour",
    0,
    23
)

high_amount_flag = st.selectbox(
    "High Amount Flag",
    [0,1]
)

night_transaction = st.selectbox(
    "Night Transaction",
    [0,1]
)

rapid_transaction = st.selectbox(
    "Rapid Transaction",
    [0,1]
)

# Prediction button
if st.button("Predict Fraud"):

    input_data = np.array([[
        amount,
        transaction_hour,
        high_amount_flag,
        night_transaction,
        rapid_transaction
    ]])

    input_scaled = scaler.transform(input_data)

    fraud_probability = model.predict_proba(
        input_scaled
    )[0][1]

    st.write(
        f"Fraud Probability: {fraud_probability:.4f}"
    )

    if fraud_probability >= 0.7:

        st.error("High Risk Fraud Transaction")

    elif fraud_probability >= 0.3:

        st.warning("Medium Risk Transaction")

    else:

        st.success("Low Risk Transaction")

