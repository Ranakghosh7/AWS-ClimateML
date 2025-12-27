import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Example dataset (replace with real one later)
data = pd.read_csv("rainfall.csv")

X = data.drop("RainTomorrow", axis=1)
y = data["RainTomorrow"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

pickle.dump(model, open("model/model.pkl", "wb"))

print("Model trained and saved")
