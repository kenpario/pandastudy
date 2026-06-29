import pandas as pd

df = pd.read_csv("data.csv")
df_json = pd.read_json("data.json")

print(df.to_string())
print(df_json)
