# import statements
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read the csv
data = pd.read_csv('maoriparliamentdata.csv')

# create the plot
plt.figure(figsize=(12, 6))

# plot the original data points
plt.plot(data['Year'], data['Percentage'], 'o', color='blue', label='Data')

# fit a polynomial of degree 2 (quadratic) to the data
coeffs = np.polyfit(data['Year'], data['Percentage'], 4)
poly_eq = np.poly1d(coeffs)

# generate x values for the line
x_range = np.linspace(data['Year'].min(), data['Year'].max(), 500)
y_fit = poly_eq(x_range)

# plot the fit line
plt.plot(x_range, y_fit, color='red', label='Best Fit Curve')

# create labels
plt.xlabel('Year')
plt.ylabel('Percentage of Māori MPs (%)')
plt.title('Percentage of Māori MPs in New Zealand Parliament Over Time')

# set scale
plt.xticks(range(int(data['Year'].min()), int(data['Year'].max()) + 1, 5))
plt.yticks([i * 0.02 for i in range(int(data['Percentage'].min() / 0.02), int(data['Percentage'].max() / 0.02) + 1)])

# display the graph
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
