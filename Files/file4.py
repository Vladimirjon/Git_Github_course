import numpy as np

import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(-10, 10, 400)

# Calculate y values
y = x

# Create the plot
plt.plot(x, y, label='y = x')

# Add title and labels
plt.title('Plot of y = x')
plt.xlabel('x')
plt.ylabel('y')

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()