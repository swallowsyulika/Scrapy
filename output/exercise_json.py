import json

data = {
    "name": "Yulika",
    "score": "98",
    "email": "Yulika@gmail.com"
}

json_str = json.dumps(data)     # dumps() turn data to .json
print(json_str)
data2 = json.loads(json_str)    # loads() turn .jsin to dict
print(data2)

jsonwtfile = "Example2.json"
with open(jsonwtfile, "w") as wt:
    json.dump(data, wt)         # dump() to save data into wt

jsonrdfile = "Example.json"
with open(jsonrdfile) as rd:
    rddata = json.load(rd)
rd_str = json.dumps(rddata)
print(rd_str)

# load vs. loads
'''
json.load is used to load json data from file. 
json.loads is used to load json string. 
Other answers are right, json.load() is used to read json from a file 
and json.loads() to read json from a string.
'''
