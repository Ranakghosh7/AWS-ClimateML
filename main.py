import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

def train_model(filename, target_column):
    df = pd.read_csv(filename)

    X = df.drop(columns=[target_column])
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=200)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print("R^2:", r2_score(y_test, preds))
    print("MAE:", mean_absolute_error(y_test, preds))

    # Feature importance
    importance = pd.DataFrame({
        "feature": X.columns,
        "importance": model.feature_importances_
    })
    importance.to_csv("feature_importance.csv", index=False)

    print("Model trained! Feature importances saved.")

if __name__ == "__main__":
    train_model("dataset.csv", "target")   
