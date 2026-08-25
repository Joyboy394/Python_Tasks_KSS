from random import randint
from sklearn.linear_model import LinearRegression

# Define parameters for training data generation
TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100

# Initialize empty lists for inputs and outputs
TRAIN_INPUT = []
TRAIN_OUTPUT = []

# Generate training data following: f(a, b, c) = 10a + 2b + 3c
for _ in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    
    # Target function
    op = (10 * a) + (2 * b) + (3 * c)
    
    TRAIN_INPUT.append([a, b, c])
    TRAIN_OUTPUT.append(op)

# Initialize and train the Linear Regression model
predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

# Test the trained model
X_TEST = [[10, 20, 30]]  # Expected outcome: 10*10 + 2*20 + 3*30 = 230
outcome = predictor.predict(X=X_TEST)
coefficients = predictor.coef_

# Display results
print(f"Outcome: {outcome}")
print(f"Coefficients: {coefficients}")
