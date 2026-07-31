import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Day 8/student_scores.csv")

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

predicted = model.predict(X_test)

result = pd.DataFrame({
    "Study Hours": X_test["Hours"],
    "Actual Score": y_test,
    "Predicted Score": predicted
})

print(result)