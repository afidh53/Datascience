import numpy as np

# 1. Input a 2x2 matrix from the user
print("Enter elements of the Matrix:")
matrix = np.array([[int(input()) for j in range(2)] for i in range(2)])

print("\n--- Your Matrix ---")
print(matrix)

print("            MATRIX STATISTICS             ")

# 2. SUM
print(f"Overall Sum  : {np.sum(matrix)}")
print(f"Column Sums  : {np.sum(matrix, axis=0)}  (axis=0)")
print(f"Row Sums     : {np.sum(matrix, axis=1)}  (axis=1)")
print("-" * 42)

# 3. MEAN (Average)
print(f"Overall Mean : {np.mean(matrix)}")
print(f"Column Means : {np.mean(matrix, axis=0)}  (axis=0)")
print(f"Row Means    : {np.mean(matrix, axis=1)}  (axis=1)")
print("-" * 42)

# 4. MAX (Maximum Value)
print(f"Overall Max  : {np.max(matrix)}")
print(f"Column Maxes : {np.max(matrix, axis=0)}  (axis=0)")
print(f"Row Maxes    : {np.max(matrix, axis=1)}  (axis=1)")
print("-" * 42)

# 5. MIN (Minimum Value)
print(f"Overall Min  : {np.min(matrix)}")
print(f"Column Mins  : {np.min(matrix, axis=0)}  (axis=0)")
print(f"Row Mins     : {np.min(matrix, axis=1)}  (axis=1)")

