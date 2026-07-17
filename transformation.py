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

print("\nElement-wise Multiplication:")
print(A * B)

print("\nElement-wise Division:")
print(A / B)



print("\nTranspose of Matrix A:")
print(A.T)

det_A = np.linalg.det(A)
print("\nDeterminant of Matrix A:")
print(round(det_A, 4))
print("\nReshape Matrix A (to 1x4):")
print(A.reshape(1, 4))

print("\nInverse of Matrix A:")
if det_A != 0:
    print(np.linalg.inv(A))
else:
    print("Matrix A is singular (determinant is 0) and cannot be inverted.")