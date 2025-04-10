from config import DATA_PATH, RESULTS_DIR
from preprocess import load_and_preprocess
from train import train_models
from evaluate import evaluate_models

def main():
    X, y, encoders = load_and_preprocess(DATA_PATH)
    models, X_test, y_test = train_models(X, y)
    results = evaluate_models(models, X_test, y_test, RESULTS_DIR)

    for name, metrics in results.items():
        print(f"{name}: MAE = {metrics['MAE']:.2f}, R2 = {metrics['R2']:.2f}")

if __name__ == "__main__":
    main()
