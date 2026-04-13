import streamlit as st
import pandas as pd
import joblib
import os

# Set Page Config
st.set_page_config(page_title="Fraud Guard", page_icon="🛡️", layout="centered")

# Load model with path safety
model_path = os.path.join("models", "model.pkl")
if not os.path.exists(model_path):
    st.error(f"Model file not found at {model_path}. Please ensure the model exists.")
    st.stop()

model = joblib.load(model_path)

# Fix for XGBoost version mismatch AttributeErrors
xgboost_params = [
    "use_label_encoder", "gpu_id", "importance_type", "n_estimators", 
    "predictor", "monotone_constraints", "interaction_constraints", 
    "num_parallel_tree", "tree_method", "validate_parameters", "base_score"
]
for attr in xgboost_params:
    if not hasattr(model, attr):
        setattr(model, attr, None)
if not hasattr(model, "use_label_encoder") or model.use_label_encoder is None:
    model.use_label_encoder = False

# Sidebar UI
st.sidebar.title("🛡️ Fraud Guard")
st.sidebar.info("A machine learning system to detect fraudulent financial transactions with high precision.")

# Main UI
st.title("💳 Financial Fraud Detection")
st.markdown("---")
st.write("Fill in the transaction details below to evaluate the fraud risk.")

# Input Form
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    with col1:
        amount = st.number_input("Transaction Amount ($)", min_value=0.0, format="%.2f")
        oldbalanceOrg = st.number_input("Source Old Balance ($)", min_value=0.0, format="%.2f")
    with col2:
        oldbalanceDest = st.number_input("Destination Old Balance ($)", min_value=0.0, format="%.2f")
        st.write("**Transaction Type**")
        type_transfer = st.checkbox("TRANSFER")
        type_cashout = st.checkbox("CASH_OUT")
    
    submit = st.form_submit_button("Predict Fraud Risk")

if submit:
    # Feature Engineering
    balance_diff_org = oldbalanceOrg - amount
    amount_ratio = amount / (oldbalanceOrg + 1)
    is_zero_balance = int(balance_diff_org == 0)
    
    input_data = pd.DataFrame([{
        'step': 1,
        'amount': amount,
        'oldbalanceOrg': oldbalanceOrg,
        'oldbalanceDest': oldbalanceDest,
        'isFlaggedFraud': 0,
        'balance_diff_org': balance_diff_org,
        'balance_diff_dest': 0,
        'amount_ratio': amount_ratio,
        'is_zero_balance': is_zero_balance,
        'type_CASH_OUT': int(type_cashout),
        'type_DEBIT': 0,
        'type_PAYMENT': 0,
        'type_TRANSFER': int(type_transfer)
    }])
    
    # Ensure exact column order expected by the model
    expected_columns = [
        'step', 'amount', 'oldbalanceOrg', 'oldbalanceDest', 'isFlaggedFraud',
        'balance_diff_org', 'balance_diff_dest', 'amount_ratio', 'is_zero_balance',
        'type_CASH_OUT', 'type_DEBIT', 'type_PAYMENT', 'type_TRANSFER'
    ]
    input_data = input_data[expected_columns]
    
    # Prediction
    prob = model.predict_proba(input_data)[0][1]
    
    st.markdown("### 🔍 Prediction Result")
    if prob > 0.7:
        st.error(f"🚨 **HIGH RISK FRAUD TRANSACTION** (Probability: {prob:.2%})")
        st.warning("Immediate investigation is recommended for this transaction.")
    else:
        st.success(f"✅ **NORMAL TRANSACTION** (Probability: {prob:.2%})")
        st.info("The transaction pattern appears consistent with legitimate activity.")
