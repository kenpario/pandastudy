import pandas as pd

df = pd.read_csv("data.csv")

# df = df.drop(columns=["Legendary", "No"])

# df = df.dropna(subset=["Type2"])

# df = df.fillna({"Type2": "None"})

# df["Type1"] = df["Type1"].replace({"Grass": "GRASS", "Dragon": "DRAGON"})

# df["Name"] = df["Name"].str.lower()

df["Legendary"] = df["Legendary"].astype(bool)

print(df.to_string())
