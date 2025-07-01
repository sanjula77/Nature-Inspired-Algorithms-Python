import numpy as np

# Define a 1D array
arr = np.array([3, 7, 2, 9, 5])
print("Original array:", arr)
print("Original shape:", arr.shape)

# Change the array to 2D (e.g., 1 row, 5 columns)
arr_2d = arr.reshape(1, 5)
print("Reshaped to 2D (1x5):", arr_2d)
print("New shape:", arr_2d.shape)

# Change the array to 2D (e.g., 5 rows, 1 column)
arr_2d_col = arr.reshape(5, 1)
print("Reshaped to 2D (5x1):", arr_2d_col)
print("New shape:", arr_2d_col.shape)

# Calculate maximum, minimum, and sum
print("Array:", arr)
print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Sum:", np.sum(arr))

# Generate 5 random numbers from a uniform distribution between 0 and 1
uniform_samples = np.random.uniform(0, 1, 5)
print("Uniform distribution samples:", uniform_samples)

# Generate 5 random numbers from a normal distribution (mean=0, std=1)
normal_samples = np.random.normal(0, 1, 5)
print("Normal distribution samples:", normal_samples)

