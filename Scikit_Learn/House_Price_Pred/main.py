import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

# Regressors
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Feature columns used in the dataset
features = [
    "bedrooms", "bathrooms", "sqft_living", "sqft_lot", "floors",
    "waterfront", "view", "condition", "grade", "sqft_above",
    "sqft_basement", "yr_built", "yr_renovated", "zipcode",
    "lat", "long", "sqft_living15", "sqft_lot15"
]

# 1. Dataset Loading Strategy (Local -> Fallback Synthetic Generator)
file_path = r"Scikit_Learn\House Price Prediction\kc_house_data.csv"

if os.path.exists(file_path):
    dataset = pd.read_csv(file_path)
elif os.path.exists("kc_house_data.csv"):
    dataset = pd.read_csv("kc_house_data.csv")
else:
    print("Local dataset file missing. Generating synthetic King County dataset locally...")
    np.random.seed(0)
    n_samples = 1000
    
    # Generate mock features matching the King County dataset schema
    data = {col: np.random.randn(n_samples) * 10 + 50 for col in features}
    # Create realistic synthetic target variable (Price)
    data["price"] = (
        data["sqft_living"] * 300 + 
        data["bedrooms"] * 5000 + 
        data["grade"] * 10000 + 
        np.random.randn(n_samples) * 5000
    )
    dataset = pd.DataFrame(data)

print("Dataset Head:")
print(dataset.head(10))

# 2. Splitting x (features) and y (target)
x = dataset[features].values
y = dataset["price"].values

print('-' * 80)
print(f"Shape of x is {x.shape}\nShape of y is {y.shape}")

# 3. Splitting into training set and test dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

print('-' * 80)
print(f"Length of X test: {len(x_test)} \nLength of X train: {len(x_train)}") 
print(f"Length of Y test: {len(y_test)} \nLength of Y train: {len(y_train)}") 

# 4. Imputation and Scaling
imputer = SimpleImputer(strategy="mean")
x_train = imputer.fit_transform(x_train)
x_test = imputer.transform(x_test)

sc = StandardScaler()
x_train_scaled = sc.fit_transform(x_train)
x_test_scaled = sc.transform(x_test)

# 5. Define Models
models = {
    "Support Vector Machine (SVR)": (SVR(), x_train_scaled, x_test_scaled),
    "Linear Regression": (LinearRegression(), x_train_scaled, x_test_scaled),
    "Decision Tree Regressor": (DecisionTreeRegressor(random_state=0), x_train, x_test),
    "Random Forest Regressor": (RandomForestRegressor(n_estimators=100, random_state=0), x_train, x_test)
}

# 6. Train and Evaluate
print('\n' + '=' * 20 + ' Model Accuracy Evaluation (R2 Score) ' + '=' * 20)
for name, (model, train_x, test_x) in models.items():
    model.fit(train_x, y_train.ravel())
    y_pred = model.predict(test_x)
    accuracy = r2_score(y_test, y_pred)
    
    print(f"\n{name}:")
    print(f"Accuracy (R2 Score): {accuracy:.2%}")
    