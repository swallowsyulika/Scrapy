import pandas as pd

# s = pd.Series([12, 29, 72, 4, 8, 10])
# print(s)

commodity = ["apple", "pen", "my son", "car"]
price = [25, 12, 0, 1000]

s = pd.Series(price, index=commodity)
print(s)
print(s.index)
print(s.values)
print("my son's cost :", s["my son"])
print(s[["apple", "car", "my son"]])
print("-"*20)
print(s*2+5)


