# 📊 Telco Customer Churn Analysis

## 📌 Project Overview
This project analyzes customer churn behavior in a telecom company using data analysis and machine learning techniques. The goal is to identify key factors influencing churn and provide actionable insights to improve customer retention.

---

## 🎯 Objectives
- Understand patterns behind customer churn
- Identify high-risk customers
- Analyze revenue loss due to churn
- Build a predictive model for churn

---

## 📂 Dataset
- Telco Customer Churn Dataset
- Contains customer details like:
  - Demographics
  - Services subscribed
  - Contract type
  - Billing information

---

## 🧹 Data Preprocessing
- Converted categorical target variable (`Churn`) into numerical format (0/1)
- Handled missing values in `TotalCharges`
- Removed `Churn Reason` column to avoid data leakage
- Encoded categorical variables
- Cleaned inconsistent values like `"No internet service"`

---

## 📊 Exploratory Data Analysis (EDA)

### 🔹 Key Insights

- **Tenure vs Churn**
  - Customers with lower tenure are more likely to churn

- **Payment Method vs Churn**
  - Customers using electronic check show higher churn

- **Internet Service vs Churn**
  - Fiber optic users have the highest churn rate
  - Customers without internet service have minimal churn

- **Contract Type vs Revenue Loss**
  - Month-to-month contracts contribute the highest revenue loss
  - Long-term contracts (1-year, 2-year) are more stable

---

## 💡 Business Insights
- Focus on retaining **new customers**
- Encourage **long-term contracts**
- Promote **automatic payment methods**
- Improve service quality for **fiber optic users**

---

## 🤖 Model Building
- Applied machine learning models like:
  - Logistic Regression
- Evaluated model performance using:
  - Accuracy
  - Confusion Matrix

---
## 📁 Project Structure
```
telco-churn-project/
│
├── data/
│   ├── raw/                     # Original dataset
│   ├── processed/              # Cleaned dataset
│
├── notebooks/
│   ├── 01_eda.ipynb            # Exploratory Data Analysis
│   ├── 02_feature_engineering.ipynb
│   ├── 03_modeling.ipynb
│
├── src/
│   ├── data_preprocessing.py   # Cleaning & transformation
│   ├── feature_engineering.py
│   ├── model.py                # ML model logic
│
├── outputs/
│   ├── plots/                  # Saved graphs
│   ├── results/                # Model results
│
├── README.md                   # Project documentation
├── requirements.txt            # Dependencies
└── .gitignore                  # Ignored files
```
---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 🚀 Future Improvements
- Use advanced models (Random Forest, XGBoost)
- Deploy model using Flask/Streamlit
- Integrate real-time prediction system

---

## 📌 Conclusion
This project highlights key factors affecting customer churn and provides actionable insights to reduce churn and improve business revenue.

---
