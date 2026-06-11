import pandas as pd

df = pd.DataFrame({
  "Name": ["Alice", "Bob", "Charlie"],
  "Salary": [50000, 60000, 70000]
})

print(df)
print(df["Name"])
print(df["Salary"])