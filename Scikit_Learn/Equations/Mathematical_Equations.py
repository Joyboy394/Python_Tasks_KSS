from random import randint
from sklearn.linear_model import LinearRegression

# 1. Configuration parameters
TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 1000

TRAIN_INPUT = []
TRAIN_OUTPUT = []

# 2. Generate training data: f(a, b, c, d) = 7a + 3b + 4c + 9d
for _ in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    d = randint(0, TRAIN_SET_LIMIT)
    
    # Calculate target output
    y = (7 * a) + (3 * b) + (4 * c) + (9 * d)
    
    TRAIN_INPUT.append([a, b, c, d])
    TRAIN_OUTPUT.append(y)

# 3. Train the Linear Regression model
predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

# 4. Test the model with sample inputs [a=10, b=20, c=30, d=40]
# Expected Output: 7(10) + 3(20) + 4(30) + 9(40) = 70 + 60 + 120 + 360 = 610
X_TEST = [[10, 20, 30, 40]]

predicted_outcome = predictor.predict(X=X_TEST)
learned_coefficients = predictor.coef_
intercept = predictor.intercept_

# 5. Output results
print(f"Test Input (a, b, c, d): {X_TEST[0]}")
print(f"Predicted Value: {predicted_outcome[0]:.2f}")
print(f"Learned Coefficients: {learned_coefficients}")
print(f"Model Intercept: {intercept:.4f}")
