import pandas as pd

data = {"Name": ["Spongebob", "Patrick", "Squidward"],
        "Age": [20, 25, 45]}

df = pd.DataFrame(data)

# Add new column

df["Job"] = ["Cook", "Intern", "Manager"]

# Add new row

new_rows = pd.DataFrame([{"Name": "Sandy", "Age": 22, "Job": "Engineer"},
                         {"Name": "Plankton", "Age": 35, "Job": "CEO"}], index=[3, 4])

df = pd.concat([df, new_rows])

print(df)
