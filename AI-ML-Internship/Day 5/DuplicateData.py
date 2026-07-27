import pandas as pd

#Q1: Create a DataFrame with duplicate rows.
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
    'Age': [25, 30, 35, 25],
    'Marks': [85, 90, 88, 85]
})

#Q2: Print the DataFrame.
print("Original DataFrame:")
print(df)

#Q3: Find duplicate rows using duplicated().
print("\nDuplicate rows (True = duplicate):")
print(df.duplicated())

#Q4: Count the number of duplicate rows.
print("\nCount of duplicate rows:")
print(df.duplicated().sum())

#Q5: Remove duplicate rows.
df_cleaned = df.drop_duplicates()

#Q6: Print the cleaned DataFrame.
print("\nDataFrame after removing duplicate rows:")
print(df_cleaned)

#Q7: Add a new row to the DataFrame.

new_row = pd.DataFrame({
    'Name': ['David'],
    'Age': [40],
    'Marks': [92]
})

df_new = pd.concat([df, new_row], ignore_index=True)

#Q8: Remove the third row.
df_new = df_new.drop(df_new.index[2])

#Q9: Reset the DataFrame index.
df_new = df_new.reset_index(drop=True)

#Q10: Print the final DataFrame.
print("\nFinal DataFrame:")
print(df_new)