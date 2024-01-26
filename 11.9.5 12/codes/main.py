import numpy as np
import matplotlib.pyplot as plt

# Define x(n)
def x_n(n):
    return np.where(n < 0, 0, 11 + 2 * n)

# Get N from the user
print("//This program will plot the terms of the sequence up to x(n)// \n")
N = int(input("Enter the value of n: "))

# Generate the sequence up to N using numpy
n_values = np.arange(-2, N + 1)
x_values = x_n(n_values)

# Plot the terms
plt.stem(n_values, x_values, markerfmt='o', linefmt='b-', basefmt='r-')
plt.title('Terms of the Sequence x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.show()

