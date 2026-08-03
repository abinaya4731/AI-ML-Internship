import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("student_scores.csv")

# Select feature and target
X = df[["Hours"]]
y = df["Scores"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Get user input
hours = float(input("Enter study hours: "))

# Validate input
if hours < 0:
    print("Study hours cannot be negative.")
else:
    prediction = model.predict([[hours]])
    print(f"Predicted Score: {prediction[0]:.2f}")