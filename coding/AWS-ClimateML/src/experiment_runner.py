# src/experiment_runner.py
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.datasets import make_classification

# 1. Generate Patterned Data (Simulating complex weather patterns)
# We create data where features interact in complex ways (hard for Logistic Reg, easy for Random Forest)
X, y = make_classification(
    n_samples=1000,
    n_features=5,
    n_informative=3, # 3 features actually matter
    n_redundant=0,
    n_clusters_per_class=2,
    random_state=42
)

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Define the Models to Compare
models = {
    "Logistic Regression (Baseline)": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(max_depth=5),
    "Random Forest (Proposed)": RandomForestClassifier(n_estimators=100, random_state=42)
}

# 3. Run Experiment
results = []
print("🧪 Running Benchmarking Experiment...")

for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    
    acc = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds)
    
    results.append({
        "Model": name,
        "Accuracy": f"{acc:.4f}",
        "F1-Score": f"{f1:.4f}"
    })

# 4. Output Results as a Markdown Table

print("| Model | Accuracy | F1-Score |")
print("|-------|----------|----------|")
for res in results:
    print(f"| {res['Model']} | {res['Accuracy']} | {res['F1-Score']} |")
print("\n---------------------------------------------")
