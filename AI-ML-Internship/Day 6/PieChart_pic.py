import matplotlib.pyplot as plt

# Q1: Create labels.
labels = ['A', 'B', 'C', 'D']

# Q2: Create values.
values = [30, 25, 20, 25]

# Q3: Plot a pie chart.
plt.pie(values, labels=labels)

# Q4: Show percentages.
plt.pie(values, labels=labels, autopct='%1.1f%%')

# Q5: Add a title.
plt.title("Pie Chart Example")

# Display the chart.
plt.show()