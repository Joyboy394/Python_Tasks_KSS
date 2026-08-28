import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Classifiers
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# 1. Load Dataset directly from sklearn (No CSV or Seaborn required)
raw_data = load_iris()
dataset = pd.DataFrame(data=raw_data.data, columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'])
dataset['Species'] = raw_data.target_names[raw_data.target]

print("Dataset Head:")
print(dataset.head())

# 2. Selecting features (X) and target (y)
X = dataset[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values
y = dataset['Species'].values

print('-' * 80)
print(f'Shape of X is {X.shape}\nShape of y is {y.shape}')

# 3. Splitting dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

print('-' * 80)
print(f"Length of X_train: {len(X_train)}\nLength of X_test: {len(X_test)}")
print(f"Length of y_train: {len(y_train)}\nLength of y_test: {len(y_test)}")

# 4. Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# 5. Define Models dictionary
models = {
    "Support Vector Machine (SVM)": SVC(),
    "Logistic Regression": LogisticRegression(),
    "Naive Bayes": GaussianNB(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(random_state=0)
}

# 6. Train, Predict, and Evaluate
print('\n' + '=' * 20 + ' Model Accuracy Evaluation ' + '=' * 20)
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n{name}:")
    print(f"Accuracy Score on the Test set: {accuracy:.0%}")
    
