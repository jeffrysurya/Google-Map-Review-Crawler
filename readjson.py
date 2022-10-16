import json


with open ('300.json') as json_file:
    data = json.load(json_file)
json.stringify(data)
print (data)

json.stringify