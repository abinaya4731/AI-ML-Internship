#Q1: Import Pandas.
import pandas as pd

#Q2: Create a DataFrame with Name and Age.
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29]
})

#Q3: Print the DataFrame.
print(df)

#Q4: Add a Marks column.
df['Marks'] = [85, 92, 78, 96, 88]

#Q5: Print the updated DataFrame.
print(df)   

#Q6: Print only the Name column.
print(df['Name'])

#Q7: Print only the Age column.
print(df['Age'])

#Q8: Print the first two rows.
print(df.head(2))

#Q9: Print the last two rows.
print(df.tail(2))

#Q10: Print DataFrame information.
print(df.info())

#Q11: Print DataFrame summary.
print(df.describe())