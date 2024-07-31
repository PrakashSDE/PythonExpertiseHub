import pandas as pd

# filter specific columns from a dataframe
df = pd.read_csv("D:/Beezlabs/Python/pandas/pokemon_data.csv")
Speed = df["Speed"]
Name_Speed = df[["Name", "Speed"]]
print(Speed.head(5))
print(Name_Speed.head(5))

# filter specific rows from a dataframe
print(df.iloc[1:4])
# withput iloc
print(df[1:4])

# filter specific rows and columns from a dataframe
print(df.iloc[1:4, 1:4])
print(df.iloc[1:4, [1, 4, 7]])

# filter specific with condition
print(df[df["Type 1"] == "Fire"])
print(df[df["Type 1"] == "Fire"].head(5))
print(df[df["Type 1"] == "Fire"].reset_index(drop=True).head(5))

# filter with multiple conditions
print(df[(df["Type 1"] == "Fire") & (df["Type 2"] == "Flying")].head(5))

# isin function
print(df[df["Type 1"].isin(["Fire", "Grass"])].head(5))

# notna function :The notna() conditional function returns a True for each row the values are not a Null value.

