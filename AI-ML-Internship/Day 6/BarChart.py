#Q1: Import Matplotlib.
import matplotlib.pyplot as plt

#Q2: Create X values from 1 to 5.
x_values = [1, 2, 3, 4, 5]

#Q3: Create Y values.
y_values = [2, 4, 6, 8, 10]

#Q4: Plot a bar chart.
plt.bar(x_values, y_values)

#Q5: Add a title and axis labels.
plt.title("Bar Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

#Q6: Display the chart.
plt.show()