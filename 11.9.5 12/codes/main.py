import numpy as np
import matplotlib.pyplot as plt

# Load data from the output.dat file
file_path = 'output.dat'


def x_n(n):
    return np.where(n < 0, 0,np.loadtxt(file_path))
    
# Generate n values from -2 to 10
n_values = np.arange(-2, 11)
x_values = x_n(n_values)

# Plot the graph
plt.stem(n_values, x_values, markerfmt='o', linefmt='b-', basefmt='r-')
plt.title('Graph of Sequence x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.show()
