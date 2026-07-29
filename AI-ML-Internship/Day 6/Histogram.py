import matplotlib.pyplot as plt

#Create a list of marks.
marks = [55, 67, 45, 78, 90, 88, 76, 95, 82, 70]    

#Plot a histogram.
plt.hist(marks, bins=5, color='blue', edgecolor='black')    

#Add a title.
plt.title("Histogram Example")

#Add X-axis and Y-axis labels.
plt.xlabel("Marks") 
plt.ylabel("Frequency")

#Display the chart.
plt.show()