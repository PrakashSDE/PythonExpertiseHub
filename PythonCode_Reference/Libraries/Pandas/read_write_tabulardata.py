from multiprocessing import connection

import pandas as pd

csv_data = pd.read_csv("D:/Beezlabs/Python/pandas/pokemon_data.csv")
excel_data = pd.read_excel("D:/Beezlabs/Python/pandas/pokemon_data.xlsx")
json_data = pd.read_json("D:/Beezlabs/Python/pandas/pokemon_data.json")

print(excel_data.head(5))
print(json_data.head(5))
print(csv_data.tail(2))

# Write data to csv, excel, json
csv_data.to_csv("D:/Beezlabs/Python/pandas/pokemon_data", index=False)
excel_data.to_excel("D:/Beezlabs/Python/pandas/pokemon_data.xlsx", index=False)
json_data.to_json("D:/Beezlabs/Python/pandas/pokemon_data.json")
