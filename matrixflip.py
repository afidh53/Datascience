import numpy as np


print("Enter elements of the Matrix:")
matrix = np.array([[int(input()) for j in range(2)] for i in range(2)])

print("\n--- Original Matrix ---")
print(matrix)

print("\nHorizontal Flip (Left to Right):")
horizontal_flip = np.fliplr(matrix)
print(horizontal_flip)

print("\nVertical Flip (Upside Down):")
vertical_flip = np.flipud(matrix)
print(vertical_flip)

print("\nFlipped on Both Axes (Fully Inverted):")
both_flip = np.flip(matrix)
print(both_flip)