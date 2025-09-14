import pandas as pd

data = {
  "Name":["Raj","Ajay","Anil","Rohit","Ritesh"],
  "maths":[67,89,78,87,77],
  "science":[95, 89, 76, 80, 85],
  "english":[78, 85, 90, 88, 82]
}

df = pd.DataFrame(data)
df["total"] = df[["maths","science","english"]].sum(axis=1)
df["Average"] = df[["maths","science","english"]].mean(axis=1)
topper = df.loc[df["total"].idxmax()]
print("Student Marks Data:\n", df)
print("\ntopper:")
print(topper)