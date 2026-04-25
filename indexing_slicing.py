import numpy as np

# Accessing elements
"""
array[index] -> for 1D array
array[row, column] -> for 2D array
"""

marks = np.array([18, 15, 14])
print(marks[0])

marks_2d = np.array([
    [18, 15, 14],
    [19, 15, 18]
])
print(marks_2d[0, 2])


# Slicing arrays
"""
array[start:stop:step]
"""

marks = np.array([18, 16, 15, 11, 13, 15, 14])

print(marks[0:4])
print(marks[3:])
print(marks[0:5:2])
print(marks[::-1])


# Fancy indexing - selecting multiple elements at once
marks = np.array([18, 16, 15, 11, 13, 15, 14])
print(marks[[0, 4, 6]])


# Boolean masking - returning elements based on conditions
marks = np.array([18, 16, 15, 11, 13, 15, 14])
print(marks[marks > 15])