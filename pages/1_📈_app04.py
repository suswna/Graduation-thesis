# 前5妊娠期构建web
import streamlit as st
import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt  # Import Matplotlib

# Load the GBDT model using joblib
model_path = "./data/gbdt_model_rf纤维妊娠期.pkl"
gbdt_model = joblib.load(model_path)

# Streamlit UI
st.title("Birth Litter Weight Prediction")

# Add input fields for the 10 features
parity = st.number_input("Parity", min_value=1, value=3)
g_adfip2 = st.number_input("G.ADFIp2", min_value=0.0, value=2.61)
g_adfip3 = st.number_input("G.ADFIp3", min_value=0.0, value=2.47)
g_d110bf = st.number_input("G.d110BF", min_value=0, value=19)
g_adfip4 = st.number_input("G.ADFIp4", min_value=0.0, value=3.06)


# Create a DataFrame with the input values
input_data = pd.DataFrame({
    "Parity": [parity],
    "G.ADFIp2": [g_adfip2],
    "G.ADFIp3": [g_adfip3],
    "G.d110BF": [g_d110bf],
    "G.ADFIp4": [g_adfip4]
})

# Make predictions using the GBDT model
prediction = gbdt_model.predict(input_data)

# Display the predicted Birth Litter Weight
st.subheader("Predicted Birth Litter Weight")
st.write(prediction[0])

# Explain the prediction using SHAP
explainer = shap.Explainer(gbdt_model)
shap_values = explainer(input_data)
st.subheader("SHAP Force Plot")
plt.figure(figsize=(20,4))  # Set figure size for better visibility
shap.plots.force(explainer.expected_value[0], shap_values.values[0], input_data, matplotlib=True)
st.pyplot(plt.gcf())# BLW-prediction
