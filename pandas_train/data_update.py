import pandas as pd

df = pd.read_csv("products.csv")
ordinals = ["A", "B", "C", "D", "E", "F"]
df.index = ordinals

print(df.head(2))
df.loc[ordinals[0], "price"] = 21.5
df.iloc[1, 2] = 46.3    # same as loc[ordinals[1], "price"]
print(df.head(2))
print("-"*20)

s = ["home", "seven", 30.4]
df.loc[ordinals[1]] = s
print(df.head(3))
print("-"*20)
df.loc[:, "price"] = [23.4, 56.7, 12.1, 90.5, 11.2, 34.1]
print(df.head())
print("-"*20)

'''
from random import sample

df = pd.DataFrame([
    sample(range(0, 1000), 3),
    sample(range(0, 1000), 3)
])

print(df)
print("-"*20)

print(df[df > 500])
df[df > 500] = df - 100
print("-"*20)
print(df)
print("-"*20)
'''
# del

df.loc[ordinals[0], 'price'] = None
df.iloc[1, 2] = None
print(df.head(3))
print('-'*20)

df2 = df.drop(["B", "D"])
print(df2.head())
print('-'*20)
# df.drop(df.index[[2, 3]], inplace=True)
# print(df.head())
# print('-'*20)

df2 = df.drop(["price"], axis=1)    # 0 -> columns ,  1 -> rows
print(df2.head(3))
print('-'*20)

# add

df.loc["G"] = ["tec", "family", 28.5]
print(df.tail(3))
print('-'*20)

s = pd.Series({"type": "home", "name": "ok", "price": 79.2})
df2 = df.append(s, ignore_index=True)
print(df2.tail(3))
print('-'*20)

df['sales'] = [124.5, 227.5, 156.7, 435.6, 333.7, 259.8, 132.5]
print(df)
print('-'*20)

df.loc[:, "city"] = ["tw", "tw", "jp", "uk", "tw", "us", "jp"]
print(df)
print('-'*20)


