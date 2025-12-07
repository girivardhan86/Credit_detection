import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------ UI CONFIG ------------------
st.set_page_config(page_title="Credit Card Fraud Detection", page_icon="💳", layout="centered")

# ------------------ TITLE ------------------
st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details and click **Predict** to check if it's Fraud or Not.")

# ------------------ SIDEBAR THEME ------------------
theme_choice = st.sidebar.radio("Select Theme Mode", ["Light", "Dark"])

if theme_choice == "Dark":
    plt.style.use("dark_background")
else:
    plt.style.use("default")

# ------------------ FRIENDLY FEATURE NAMES ------------------
feature_names = [
    "Account Risk Score", "Payment Behavior Index", "Transaction Stability Index",
    "Fraud Risk Correlation 1", "Fraud Risk Correlation 2",
    "High-Value Purchase Indicator", "Chargeback Likelihood",
    "Merchant Trustworthiness Score", "Card Usage Frequency",
    "Suspicious Pattern Score", "Credit Utilization Ratio",
    "Geolocation Risk Factor", "Unusual Device Activity",
    "Rapid Transaction Spike Score", "Account Age Influence",
    "Recurring Payment Indicator", "IP Address Mismatch Score",
    "Odd Hour Activity Score", "High-Risk Merchant Indicator",
    "Multiple Card Usage Flag", "Customer Spending Profile",
    "Cross-Border Transaction Flag", "Amount Rounding Anomaly",
    "High Volume Merchant Pattern", "Low-Frequency Purchase Flag",
    "Identity Verification Risk", "Velocity Check Score",
    "Unusual Category Spend", "Extra Pattern Feature 1",
    "Extra Pattern Feature 2"
]

# ------------------ INPUT FORM ------------------
st.subheader("Enter Transaction Data")

V_features = {}
for i, name in enumerate(feature_names, start=1):
    V_features[f"V{i}"] = st.number_input(f"{name}", value=0.0, step=0.1)

time_value = st.number_input("Transaction Time (seconds since first record)", value=0.0, step=0.1)
amount_value = st.number_input("Transaction Amount (USD)", value=0.0, step=1.0)

# ------------------ PREDICT BUTTON ------------------
if st.button("Predict"):
    # Simple placeholder prediction logic:
    if amount_value == 10000 or amount_value == -10000:
        prediction = 1  # Fraud
    else:
        total_score = sum(V_features.values()) + time_value + amount_value
        prediction = 1 if total_score > 10 else 0

    # Show result
    if prediction == 1:
        st.error("🚨 Transaction is Fraudulent!")
    else:
        st.success("✅ Transaction is Safe.")

    # ------------------ PIE CHART ------------------
    st.subheader("Fraud vs Non-Fraud Distribution")
    labels = ['Non-Fraud', 'Fraud']
    sizes = [0.4, 0.6] if prediction == 1 else [1, 0]  # Example percentages
    colors = ['#66b3ff', '#ff6666']

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)






















