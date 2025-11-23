import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

import warnings
warnings.filterwarnings("ignore")


def create_eda_report(df, output="eda_report.txt"):
    """Generate a simple EDA report and save to text file."""
    with open(output, "w") as f:
        f.write("===== BASIC INFO =====\n")
        f.write(str(df.info()) + "\n\n")

        f.write("===== DESCRIPTIVE STATS =====\n")
        f.write(str(df.describe()) + "\n\n")

        f.write("===== MISSING VALUES =====\n")
        f.write(str(df.isna().sum()) + "\n\n")

    print(f"[OK] EDA report saved as {output}")


def benchmark_models(X, y):
    """Train and compare ML models."""
    models = {
        "LinearRegression": LinearRegression(),
        "Ridge": Ridge(alpha=1.0),
        "RandomForest": RandomForestRegressor(n_estimators=200),
        "GradientBoosting": GradientBoostingRegressor()
    }

    results = []

    for name, model in models.items():
        pipe = Pipeline([
            ("scaler", StandardScaler()),
            ("model", model)
        ])

        scores = cross_val_score(pipe, X, y, scoring="r2", cv=5)
        results.append([name, scores.mean(), scores.std()])

        print(f"{name}: R²={scores.mean():.4f} (+/- {scores.std():.4f})")

    df_results = pd.DataFrame(results, columns=["Model", "Mean_R2", "Std_R2"])
    df_results.to_csv("model_benchmark_results.csv", index=False)

    print("\n[OK] Benchmark results saved to model_benchmark_results.csv")
    return df_results


def run_pipeline(filename, target):
    df = pd.read_csv(filename)
    print("[OK] Dataset loaded.")

    create_eda_report(df)

    X = df.drop(columns=[target])
    y = df[target]

    print("[INFO] Running model benchmark...")
    results = benchmark_models(X, y)

    print("\n===== BEST MODEL =====")
    best = results.sort_values("Mean_R2", ascending=False).iloc[0]
    print(best)


if __name__ == "__main__":
    run_pipeline("dataset.csv", "target")
