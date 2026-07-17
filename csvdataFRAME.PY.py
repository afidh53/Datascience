import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Anu", "Rahul", "Neena", "Arun", "Meera"],
    "Mark": [85, 95, 78, 88, 70]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Filter students with marks greater than 80
filtered_df = df[df["Mark"] > 80]

print("\nStudents with Marks > 80:")
print(filtered_df)

# Sort in descending order
sorted_df = filtered_df.sort_values(by="Mark", ascending=False)

print("\nSorted DataFrame (Descending Order):")
print(sorted_df)