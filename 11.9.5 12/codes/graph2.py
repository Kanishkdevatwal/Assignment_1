import numpy as np
import matplotlib.pyplot as plt

# Load data from the output2.dat file
file_path = 'output2.dat'


def y_n(n):
    return np.where(n < 0, 0, np.loadtxt(file_path))
    
# Generate n values from -2 to 10
n_values = np.arange(-2, 11)
y_values = y_n(n_values)

# Plot the graph
plt.stem(n_values, y_values, markerfmt='o', linefmt='b-', basefmt='r-')

# Highlight specific points with different colors
highlighted_points = [3, 6, 10]
for point in highlighted_points:
    plt.plot(point, y_values[n_values == point], marker='o', markersize=8, color='c', linestyle='None', label=f'y({point})')

plt.title('Terms of y(n)')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.legend()
plt.show()
