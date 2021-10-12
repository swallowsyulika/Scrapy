import pandas as pd

df = pd.read_csv("products.csv")    # encoding="utf8"
# df.columns = ["type", "name", "price"]
ordinals = ["A", "B", "C", "D", "E", "F"]
df.index = ordinals

print(df["price"].head(3))  # same as df.price.head(3)
print(df[0:3])  # not include 3
print(df["C":"E"])  # include E
print('-'*20)

# loc   [item, tag]
print(df.loc[ordinals[1]])
print(type(df.loc[ordinals[1]]))
print(df.loc[:, ["name", "price"]])
print(df.loc[["C", "F"], ["name", "price"]])    # "C":"F"
print(df.loc["C", ["name", "price"]])
# another loc's way
print(df.loc["A"]["price"])
# iloc
print(df.iloc[3])
print(df.iloc[3:5, 1:3])
print(df.iloc[[1, 2, 4], [0, 2]])
print(df.iloc[1, 1])    # smae as df.iat[1,1]
print('-'*20)


# filter data
print(df[df.price > 20])    # find the price over 20
print(df[df["type"].isin(["tec", "home"])])   # find type are tec or home
print(df[(df.price > 20) & (df.price < 25)])
print('-'*20)
df.loc["G"] = ["tec", "ok", 28.5]   # set new data
print(df[df["type"].str.startswith("t")])
print('-'*20)

df2 = df.set_index("price")
print(df2)
print('-'*20)
df2.sort_index(ascending=False, inplace=True)
print(df2)
print('-'*20)

df = df.sort_values("price", ascending=False)
print(df)
print('-'*20)
df.sort_values(["type", "price"], inplace=True)
print(df)
# print(df)
# print('-'*20)
# df.index = [i for i in range(len(df))]  # reset_index()
# print(df)

