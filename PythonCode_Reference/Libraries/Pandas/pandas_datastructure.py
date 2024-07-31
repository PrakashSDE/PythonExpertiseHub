import pandas as pd

df = pd.DataFrame({
    "Name": [
        "Braund",
        "Allen",
        "Bonnell",
    ],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"],
})
print(df)

# Each column in a DataFrame is a Series
print(type(df["Name"]))

# Now i am trying to working with age column
print(df["Age"])
my_age = df["Age"].max()
print(my_age)

# Create Series from scratch
ages = pd.Series([223, 36, 98], name="Column_Name")
print(ages.min())

# Accessing important functionality of Series and DataFrame
print(ages.describe())
print(df.describe())
print(df.info())
print(df.shape)
print(df.values)
print(df.columns)
print(df.index)
print(df.dtypes)

