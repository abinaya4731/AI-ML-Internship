import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("student_scores.csv")

# Feature and target
X = df[["Hours"]]
y = df["Scores"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# User input
hours = float(input("Enter study hours: "))

# Prediction
predicted_score = model.predict([[hours]])

print(f"Predicted Score: {predicted_score[0]:.2f}")