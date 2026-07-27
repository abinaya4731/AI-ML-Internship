#Q1: Import the Pandas library.
import pandas as pd

#Q2: Create a DataFrame with Name, Age, and Marks, including some missing values.
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, None, 35],
    'Marks': [85, None, 90, 88]
})

#Q3: Print the DataFrame.
print("Original DataFrame:")
print(df)

#Q4: Check for missing values using isnull().
print("\nMissing values (True = missing):")
print(df.isnull())

#Q5: Count the missing values in each column.
print("\nCount of missing values in each column:")
print(df.isnull().sum())

#Q6: Remove all rows containing missing values.
df_cleaned = df.dropna()
print("\nDataFrame after removing rows with missing values:")
print(df_cleaned)

#Q7: Fill all missing values with 0.
df_filled = df.fillna(0)
print("\nDataFrame after filling missing values with 0:")
print(df_filled)

#Q8: Fill the missing values in the Age column with the average age.
average_age = df['Age'].mean()
df['Age'].fillna(average_age, inplace=True)

#Q9: Fill the missing values in the Marks column with the average marks.
average_marks = df['Marks'].mean()
df['Marks'].fillna(average_marks, inplace=True) 

#Q10: Print the cleaned DataFrame.
print("\nDataFrame after filling missing values with averages:")
print(df)