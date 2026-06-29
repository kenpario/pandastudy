import pandas as pd

df = pd.read_csv("data.csv", index_col="Name")

# Selection by column

# print(df["Height"].to_string())
# print(df["Weight"].to_string())
# print(df[["Name", "Height", "Weight"]].to_string())

# Selection by row

# print(df.loc["Alakazam":"Mewtwo", ["Height", "Weight"]])

pokemon = input("Enter the name of the pokemon: ")
try:
    print(df.loc[pokemon.capitalize()])
except KeyError:
    print(f"{pokemon.capitalize()} not found")
