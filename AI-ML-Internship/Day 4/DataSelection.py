import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],    
    'Age': [24, 27, 22, 32, 29],
    'Marks': [85, 92, 78, 96, 88]
})

#Print the first row.
print(df.iloc[0])

#Print the second row.
print(df.iloc[1])

#Print the third row.
print(df.iloc[2])

#Print the first column.
print(df.iloc[:, 0])

#Print the second column.
print(df.iloc[:, 1])

#Print the Marks column.
print(df['Marks'])

#Print rows 0 to 2.
print(df.iloc[0:3])

#Print only Name and Marks columns.
print(df[['Name', 'Marks']])

#Find the maximum marks.
print(df['Marks'].max())

#Find the average marks.
print(df['Marks'].mean())