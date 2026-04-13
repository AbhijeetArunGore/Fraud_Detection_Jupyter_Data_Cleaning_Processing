# 🛡️ Fraud Guard: Financial Fraud Detection System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)
[![XGBoost](https://img.shields.io/badge/Model-XGBoost-orange.svg)](https://xgboost.readthedocs.io/)

Fraud Guard is a sophisticated machine learning application designed to detect fraudulent financial transactions. By leveraging state-of-the-art algorithms and advanced feature engineering, the system identifies high-risk patterns in real-time, helping financial institutions mitigate risk and prevent illegal activities.

## 🚀 Key Features
- **Real-time Detection:** Interactive web interface built with Streamlit for instant transaction evaluation.
- **Advanced Modeling:** Utilizes **XGBoost Classifier**, optimized for high precision and recall on imbalanced datasets.
- **Imbalance Handling:** Employs **SMOTE** (Synthetic Minority Over-sampling Technique) to ensure the model learns effectively from rare fraud cases.
- **Feature Engineering:** Includes custom-engineered features such as `balance_diff`, `amount_ratio`, and `is_zero_balance` to capture behavioral signals.
- **Robustness:** Built-in compatibility patches to handle model serialization across different library versions.

## 📂 Project Structure
```text
├── app.py                # Streamlit Web Application
├── models/
│   └── model.pkl         # Trained XGBoost Model
├── src/
│   └── model.ipynb       # Research, Data Cleaning & Model Training
├── data/
│   └── (Fraud.csv)       # Raw dataset (Excluded from repo due to size)
├── requirements.txt      # Project Dependencies
└── .gitignore            # Git exclusion rules
```

## 📊 Model Performance
The model was evaluated using a rigorous split and achieved the following metrics:
- **ROC-AUC:** ~0.999
- **Precision:** High precision to minimize false alarms.
- **Recall:** Optimized to capture as many fraud cases as possible.

## 🛠️ Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/AbhijeetArunGore/Fraud_Detection_Jupyter_Data_Cleaning_Processing.git
   cd Fraud_Detection_Jupyter_Data_Cleaning_Processing
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

## 📈 Dataset Information
The system is trained on the **Synthetic Financial Datasets For Fraud Detection** (often found on Kaggle). 
- Due to the large size (~470MB), the raw `Fraud.csv` file is not included in this repository.
- You can download the dataset from [Kaggle](https://www.kaggle.com/datasets/paysim1/paysim1) and place it in the `data/` folder for retraining.

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any suggestions.

---
*Developed with ❤️ for secure finance.*
