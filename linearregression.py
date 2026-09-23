import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# -----------------------------
# 1. Load the dataset
# -----------------------------
diabetes = load_diabetes()

X = diabetes.data
y = diabetes.target
feature_names = diabetes.feature_names

# =========================================================
# 2. Simple Linear Regression (using only BMI)
# =========================================================

# Find BMI column
bmi_index = feature_names.index('bmi')

# Select only BMI
X_bmi = X[:, bmi_index].reshape(-1, 1)

# Split data into training and testing sets
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_bmi,
    y,
    test_size=0.2,
    random_state=42
)

# Create and train Simple Linear Regression model
lin_reg = LinearRegression()
lin_reg.fit(X_train_s, y_train_s)

# Make predictions
y_pred_s = lin_reg.predict(X_test_s)

# Evaluate Simple Linear Regression
mse_s = mean_squared_error(y_test_s, y_pred_s)
r2_s = r2_score(y_test_s, y_pred_s)

print("=== Simple Linear Regression (BMI) ===")
print(f"Coefficient: {lin_reg.coef_[0]:.2f}")
print(f"Intercept:   {lin_reg.intercept_:.2f}")
print(f"MSE:         {mse_s:.2f}")
print(f"R^2 Score:   {r2_s:.4f}")
print()


# =========================================================
# 3. Multiple Linear Regression (using all features)
# =========================================================

# Split data into training and testing sets
X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create and train Multiple Linear Regression model
multi_reg = LinearRegression()
multi_reg.fit(X_train_m, y_train_m)

# Make predictions
y_pred_m = multi_reg.predict(X_test_m)

# Evaluate Multiple Linear Regression
mse_m = mean_squared_error(y_test_m, y_pred_m)
r2_m = r2_score(y_test_m, y_pred_m)

print("=== Multiple Linear Regression (all features) ===")

for name, coef in zip(feature_names, multi_reg.coef_):
    print(f"  {name:8s}: {coef:8.2f}")

print(f"Intercept:   {multi_reg.intercept_:.2f}")
print(f"MSE:         {mse_m:.2f}")
print(f"R^2 Score:   {r2_m:.4f}")
print()


# =========================================================
# 4. Compare the two models
# =========================================================

print("=== Model Comparison ===")
print(f"{'Model':<25}{'MSE':>10}{'R^2':>10}")

print(
    f"{'Simple (BMI)':<25}"
    f"{mse_s:>10.2f}"
    f"{r2_s:>10.4f}"
)

print(
    f"{'Multiple (all features)':<25}"
    f"{mse_m:>10.2f}"
    f"{r2_m:>10.4f}"
)


# =========================================================
# 5. Plot Simple Linear Regression results
# =========================================================

plt.figure(figsize=(8, 6))

# Actual test data
plt.scatter(
    X_test_s,
    y_test_s,
    color='blue',
    label='Actual',
    alpha=0.6
)

# Predicted regression line
# Sort values so the line is displayed correctly
sort_index = np.argsort(X_test_s[:, 0])

plt.plot(
    X_test_s[sort_index],
    y_pred_s[sort_index],
    color='red',
    linewidth=2,
    label='Predicted'
)

plt.xlabel('BMI (standardized)')
plt.ylabel('Disease Progression')
plt.title('Simple Linear Regression: BMI vs Disease Progression')
plt.legend()
plt.tight_layout()

# Save plot
plt.savefig('linear_regression_plot.png', dpi=150)

# Display plot
plt.show()
