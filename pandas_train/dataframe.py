import pandas as pd

products = {
    "price": [12.5, 3.75, 15.8, 19.25, 8.4],
    "activity": ["special", "special", "common", "special", "common"],
    "store": ["711", "711", "family", "family", "family"]
           }
ordinals = ["A", "B", "C", "D", "E"]
df = pd.DataFrame(products, index=ordinals)
print(df)
# df.to_html("test.html")
# df = pd.read_html
print("-"*20)

# define columns's sequence
df2 = pd.DataFrame(products, columns=["activity", "store", "price"], index=ordinals)
print(df2)
print('-'*20)

# change shape
print(df.T)
print("-"*20)

# preset is 5
print(df.head(2))
print(df.tail(2))
print("-"*20)

# info
print(df.index)
print(df.columns)
print(df.values)
print(len(df))
print(df.shape)
df.info()
print("-"*20)

# traversal
for index, row in df.iterrows():
    print(index, row["price"], row["activity"], row["store"])

# use set_index()  &  reset_index() change index
print("-"*20)

df2 = df.set_index(["activity", "store"])
df2.sort_index(ascending=False, inplace=True)
print(df2)
