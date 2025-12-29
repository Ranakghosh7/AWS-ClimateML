import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(path):
    df = pd.read_csv(path)

    # Drop rows with missing target
    df = df.dropna(subset=["RainTomorrow"])

    # Drop leakage columns (CRITICAL)
    leakage_cols = ["RainToday", "Date", "RISK_MM"]
    df = df.drop(columns=leakage_cols, errors="ignore")

    # Target
    y = df["RainTomorrow"].map({"No": 0, "Yes": 1})
    X = df.drop("RainTomorrow", axis=1)

    # Numerical features
    num_cols = X.select_dtypes(include=["float64", "int64"]).columns
    X[num_cols] = X[num_cols].fillna(X[num_cols].median())

    # Categorical features
    cat_cols = X.select_dtypes(include=["object"]).columns
    for col in cat_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))

    X["RainTomorrow"] = y
    return X