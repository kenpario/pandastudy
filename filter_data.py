import pandas as pd

data = pd.read_csv("data.csv")

tall_pokemons = data[data["Height"] >= 2]

heavy_pokemons = data[data["Weight"] >= 100]

legendary_pokemons = data[data["Legendary"] == 1]

water_pokemons = data[(data["Type1"] == "Water") | (data["Type2"] == "Water")]

fire_pokemons = data[(data["Type1"] == "Fire") & (data["Type2"] == "Flying")]

print(tall_pokemons)
print(heavy_pokemons)
print(legendary_pokemons)
print(water_pokemons)
print(fire_pokemons)
