import pandas as pd


#  Feature Engineering Function
def encode_features(df):
    
    # 1. Convert Yes/No columns to 1/0
    yes_no_cols = df.select_dtypes(include='object').columns
    
    for col in yes_no_cols:
        if set(df[col].unique()) == {'Yes', 'No'}:
            df[col] = df[col].map({'Yes': 1, 'No': 0})
    
    
    # 2. Create new feature (Avg Charges per month)
    df['Avg_Charges'] = df['Total_Charges'] / (df['Tenure_Months'] + 1)
    
    
    # 3. One-Hot Encoding for remaining categorical columns
    df = pd.get_dummies(df, drop_first=True)
    
    
    return df
