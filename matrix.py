import numpy as np

# Input two 2x2 matrices
print("Enter elements of Matrix A:")
A = np.array([[int(input()) for j in range(2)] for i in range(2)])

print("Enter elements of Matrix B:")
B = np.array([[int(input()) for j in range(2)] for i in range(2)])

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)


print("\nAddition:")
print(A + B)

print("\nSubtraction:")
print(A - B)


print("\nMultiplication:")
print(A * B)


print("\nDivision:")
print(A / B)