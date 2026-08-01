import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("student_scores.csv")

# Feature and Target
X = df[["Hours"]]
y = df["Scores"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict score for 7 study hours
prediction = model.predict([[7]])

print("Predicted Score:", prediction[0])