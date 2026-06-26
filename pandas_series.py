import pandas as pd

# data = [100, 102, 104, 105]
#
# series = pd.Series(data, index=["a", "b", "c", "d"])
#
# print(series)
# series.loc["d"] = 254
# print(series.loc["d"])
# print(series.iloc[0])
# print(series[series >= 101])

calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

series = pd.Series(calories)

series.loc["Day 3"] += 500

print(series.loc["Day 3"])

print(series[series >= 2000])
print(series[series <= 2000])
