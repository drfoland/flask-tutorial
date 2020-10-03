import json

with open("data/general.json") as file:
    data = json.load(file)

def write_data(data):
    with open("data/general.json", 'w') as file:
        json.dump(data, file)