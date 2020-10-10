import json

def read_data(filename):
    with open(f"data/{filename}.json") as file:
        data = json.load(file)
    return data
    
def write_data(data, filename):
    with open(f"data/{filename}.json", 'w') as file:
        json.dump(data, file)
