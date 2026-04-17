from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score


# Evaluate Model
def evaluate(model, X_test, y_test):
    
    # Predictions
    preds = model.predict(X_test)
    probs = model.predict_proba(X_test)[:, 1]
    
    
    # Classification Report
    print("Classification Report:\n")
    print(classification_report(y_test, preds))
    
    
    # Confusion Matrix
    print("\nConfusion Matrix:\n")
    print(confusion_matrix(y_test, preds))
    
    
    # ROC-AUC Score
    roc = roc_auc_score(y_test, probs)
    print("\nROC-AUC Score:", roc)
