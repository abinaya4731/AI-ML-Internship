import pandas as pd

df = pd.read_csv("Day 7/student_scores.csv")

X = df[["Hours"]]
y = df["Scores"]

print("Feature")
print(X)

print("\nTarget")
print(y)