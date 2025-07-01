import numpy as np

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array[3])
print(type(my_array))  # Check the type of my_array
print(my_array.ndim)   # Check the dimension of my_array

# Create a 2-dimensional array
my_2d_array = np.array([[1, 2, 3], [4, 5, 6]])
print(my_2d_array[1,2])
print(type(my_2d_array))  # Check the type of my_2d_array
print(my_2d_array.ndim)
print("Shape of my_2d_array", my_2d_array.shape)   # Check the dimension of my_2d_array

# Create a 3-dimensional array
my_3d_array = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
    [[13, 14, 15], [16, 17, 18]]
])
print(my_3d_array)
print(type(my_3d_array))  # Check the type of my_3d_array
print(my_3d_array.ndim)   # Check the dimension of my_3d_array
print("Shape of my_3d_array", my_3d_array.shape)

# Zero matrix: All elements are 0. Used for initialization or as a neutral element in addition.
zero_matrix = np.zeros((3, 3))
print(zero_matrix)

# Ones matrix: All elements are 1. Useful for testing, broadcasting, or as a base for other operations.
ones_matrix = np.ones((3, 3))
print(ones_matrix)

# Identity matrix: Diagonal elements are 1, others are 0. Used in linear algebra as the multiplicative identity.
identity_matrix = np.eye(3)
print(identity_matrix)

