import json

with open("saveddata.json", "r") as json_file:
    loaded_data = json.load(json_file)

print(loaded_data)

# after being read from a json file, the data is a python dictionary in every way
# and has no knowledge that it came from a json file
loaded_data["new_record"] = "new value"

print(loaded_data)

# to update the data stored in a json file, load it, do whatever you need to do to
# the loaded dictionary, and then overwrite the existing file

with open("savedata.json", "w") as json_file:
    json.dump(loaded_data, json_file, indent=2)