import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("student_scores.csv")

X = df[["Hours"]]
y = df["Scores"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

hours = [[2], [5], [8], [10]]

predictions = model.predict(hours)

for hour, score in zip(hours, predictions):
    print(f"Study Hours: {hour[0]} -> Predicted Score: {score:.2f}")