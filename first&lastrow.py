import pandas as pd


data = {
    "Name": ["Anu", "Reena", "Raj", "Arun", "Meera"],
    "Age": [23, 24, 25, 22, 26],
    "City": ["Kottayam", "Ernakulam", "Alappuzha", "Kochi", "Thrissur"]
}


df = pd.DataFrame(data)


df.to_csv("students.csv", index=False)


df = pd.read_csv("students.csv")


print("First Rows:")
print(df.head())


print("\nLast Rows:")
print(df.tail())