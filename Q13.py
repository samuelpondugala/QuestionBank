#Write a Python program to generate a 3*4*6 3D array whose each element is *.
# Import the numpy library
import numpy as np
# Create a 3*4*6 3D array of zeros
array = np.zeros((3, 4, 6))
# Loop through the array and replace each element with *
for i in range(3):
  for j in range(4):
    for k in range(6):
      array[i][j][k] = "*"
# Print the array
print(array)
