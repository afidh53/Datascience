import pandas as pd

df = pd.read_csv("students.csv")

print("Complete DataFrame:")
print(df)

print("\nFirst Row:")
print(df.head(1))

print("\nLast Row:")
print(df.tail(1))