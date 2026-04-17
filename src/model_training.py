import joblib
from sklearn.ensemble import RandomForestClassifier


#Train Model
def train_model(X_train, y_train):
    
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
    
    model.fit(X_train, y_train)
    
    return model


# Save Model
def save_model(model, path):
    
    joblib.dump(model, path)


#Load Model
def load_model(path):
    
    return joblib.load(path)


# Run Script (optional)
if __name__ == "__main__":
    
    from data_preprocessing import load_data, clean_data
    from feature_engineering import encode_features
    from sklearn.model_selection import train_test_split

    # Load + preprocess
    df = load_data("../data/processed/telco_clean.csv")
    df = clean_data(df)
    df = encode_features(df)

    # Split
    X = df.drop(['Churn_Value', 'Churn_Label'], axis=1)
    y = df['Churn_Value']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train
    model = train_model(X_train, y_train)

    # Save
    save_model(model, "../models/random_forest.pkl")

    print("Model trained and saved successfully!")
