import json


# Read JSON File (Display data info from file)
def read_json(path):

    with path.open("r") as file:
        data = json.load(file)
        return data

# Save JSON file (Overwrite file data with new info)
def save_json(path, data):

    with path.open("w") as file:
        json.dump(data, file, indent=4)
