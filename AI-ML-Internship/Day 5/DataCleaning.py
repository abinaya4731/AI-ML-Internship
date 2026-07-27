import pandas as pd
#Create a DataFrame with Name, Age, Marks, and City.
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Marks': [85, 90, 88, 92],
    'City': ['New York', 'London', 'Tokyo', 'Paris']
})

#Print the DataFrame.
print("Original DataFrame:")
print(df)

#Remove the Age column.
df = df.drop('Age', axis=1)

#Rename the Marks column to Score.
df = df.rename(columns={'Marks': 'Score'})

#Add a new column called Department.
df['Department'] = ['Engineering', 'Medicine', 'Business', 'Arts']

#Update the value of one student's Score.
df.loc[df['Name'] == 'Alice', 'Score'] = 95

#Sort the DataFrame by Score in ascending order.
df = df.sort_values('Score')

#Sort the DataFrame by Score in descending order.
df = df.sort_values('Score', ascending=False)

#Reset the DataFrame index.
df = df.reset_index(drop=True)

#Print the final cleaned DataFrame.
print("Final Cleaned DataFrame:")
print(df)