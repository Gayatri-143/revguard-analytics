import pandas as pd


# Load Data
def load_data(path):
    df = pd.read_csv(path)
    
    # Clean column names (remove spaces and special characters)
    df.columns = df.columns.str.replace(" ", "_")
    df.columns = df.columns.str.replace("-", "_")
    
    return df


# Clean Data
def clean_data(df):
    
    # 1. Drop unnecessary columns
    df = df.drop(columns=[
        'CustomerID',
        'Count',
        'Country',
        'State',
        'City',
        'Zip_Code',
        'Lat_Long',
        'Latitude',
        'Longitude',
        'Churn_Reason'
    ], errors='ignore')
    
    
    # 2. Convert Total_Charges to numeric
    df['Total_Charges'] = pd.to_numeric(df['Total_Charges'], errors='coerce')
    
    
    # 3. Handle missing values (fill with median)
    df.fillna(df.median(numeric_only=True), inplace=True)
    
    
    # 4. Remove duplicate rows
    df = df.drop_duplicates()
    
    
    return df
