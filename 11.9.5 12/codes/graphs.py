import numpy as np
import matplotlib.pyplot as plt

# Load data from the output.dat file
file_path_x = 'output.dat'
file_path_y = 'output2.dat'

def x_n(n):
    return np.where(n < 0, 0, np.loadtxt(file_path_x))

def y_n(n):
    return np.where(n < 0, 0, np.loadtxt(file_path_y))

# Generate n values from -2 to 10
n_values = np.arange(-2, 11)
x_values = x_n(n_values)
y_values = y_n(n_values)

# Plot the graph for x(n)
plt.stem(n_values, x_values, markerfmt='o', linefmt='b-', basefmt='r-')
plt.title('Terms of the Sequence x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.savefig('fig.png')
plt.close()

# Plot the graph for y(n)
plt.stem(n_values, y_values, markerfmt='o', linefmt='b-', basefmt='r-')

# Highlight specific points with different colors in y(n)
highlighted_points = [3, 6, 10]
highlighted_colors = ['r', 'g', 'b']  # Different colors for y(3), y(6), y(10)

for point, color in zip(highlighted_points, highlighted_colors):
    plt.plot(point, y_values[n_values == point], marker='o', markersize=8, color=color, linestyle='None', label=f'y({point})')

plt.title('Terms of y(n)')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.legend()
plt.savefig('fig2.png')
plt.close()
