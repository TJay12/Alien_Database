import json


# Read JSON File (Display data info from database_file)
def read_json(path):

    with path.open("r") as file:
        data = json.load(file)
        return data

# Save JSON database_file (Overwrite database_file data with new info)
def save_json(path, data):

    with path.open("w") as file:
        json.dump(data, file, indent=4)
