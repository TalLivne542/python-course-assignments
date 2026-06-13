import pandas as pd
import numpy as np
from sklearn.model_model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load the dataset (Assuming the file is downloaded and named concrete_data.csv)
try:
    df = pd.read_csv('concrete_data.csv')
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: 'concrete_data.csv' not found. Please download it from Kaggle first.")
    exit()

# Display basic information
print(f"Dataset shape: {df.shape}")
print("Features analyzed:", list(df.columns[:-1]))
print("Target variable:", df.columns[-1])

# 2. Split into features (X) and target (y)
X = df.iloc[:, :-1]  # All columns except the last one
y = df.iloc[:, -1]   # The last column (Compressive Strength)

# 3. Train-Test Split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize and Train the Prediction Model
print("\nTraining Random Forest Regressor model...")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Make Predictions and Evaluate
y_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\n=== Model Evaluation Results ===")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared Score (R²): {r2:.2f}")
