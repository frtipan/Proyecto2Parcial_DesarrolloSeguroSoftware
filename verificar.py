import pandas as pd

df = pd.read_csv("data/CVEfixes.csv")

print(df["safety"].value_counts())

print("\nLenguajes:\n")
print(df["language"].value_counts().head(20))