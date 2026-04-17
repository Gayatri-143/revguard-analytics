import shap
import matplotlib.pyplot as plt
import os


#  Explain Model using SHAP
def explain_model(model, X, save_path="outputs/shap_values"):
    
    # 1. Create folder if not exists
    os.makedirs(save_path, exist_ok=True)
    
    
    # 2. Initialize SHAP Explainer
    explainer = shap.TreeExplainer(model)
    
    
    # 3. Calculate SHAP values
    shap_values = explainer.shap_values(X)
    
    
    # 4. Summary Plot (feature importance)
    plt.figure()
    shap.summary_plot(shap_values, X, show=False)
    plt.savefig(f"{save_path}/summary_plot.png", bbox_inches='tight')
    plt.close()
    
    
    # 5. Bar Plot (importance ranking)
    plt.figure()
    shap.summary_plot(shap_values, X, plot_type="bar", show=False)
    plt.savefig(f"{save_path}/bar_plot.png", bbox_inches='tight')
    plt.close()
    
    
    return shap_values
