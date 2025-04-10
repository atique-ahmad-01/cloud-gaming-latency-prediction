from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import os

def evaluate_models(models, X_test, y_test, results_dir):
    results = {}
    for name, model in models.items():
        y_pred = model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        results[name] = {'MAE': mae, 'R2': r2}
        
        # Plot
        plt.figure()
        plt.scatter(y_test, y_pred, alpha=0.5)
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
        plt.xlabel("Actual")
        plt.ylabel("Predicted")
        plt.title(f"{name}: Actual vs Predicted")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(os.path.join(results_dir, f"{name.replace(' ', '_').lower()}_plot.png"))
    
    return results
