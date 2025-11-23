# data.py
import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Number of rows you want
num_rows = 2000  # You can increase this to 5000+ if needed

# Generate random features
df = pd.DataFrame({
    "feature1": np.random.randint(1, 100, num_rows),
    "feature2": np.random.randint(1, 50, num_rows),
    "feature3": np.random.rand(num_rows) * 20,
    "feature4": np.random.randint(0, 2, num_rows),  # binary feature
    "feature5": np.random.rand(num_rows) * 10,
    "feature6": np.random.randint(10, 500, num_rows),
    "feature7": np.random.rand(num_rows) * 100,
    "feature8": np.random.randint(0, 5, num_rows),
})

# Create a target column based on a combination of features + noise
df["target"] = (
    3 * df["feature1"]
    + 2 * df["feature2"]
    + 4 * df["feature3"]
    - 5 * df["feature4"]
    + 1.5 * df["feature5"]
    + 0.5 * df["feature6"]
    + 0.1 * df["feature7"]
    - 2 * df["feature8"]
    + np.random.randn(num_rows) * 10  # added noise
)

# Save to CSV
df.to_csv("dataset.csv", index=False)
print(f"[OK] dataset.csv created with {num_rows} rows and {df.shape[1]-1} features")
