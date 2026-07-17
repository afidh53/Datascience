import pandas as pd

student = {
    "Roll_No": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [20, 21, 19, 22, 20],
    "Course": ["BCA", "BCA", "BCA", "BCA", "BCA"],
    "Marks": [85, 90, 78, 88, 95]
}

df = pd.DataFrame(student)

print("Student DataFrame")
print(df)

print("\nDataFrame Information")
df.info()