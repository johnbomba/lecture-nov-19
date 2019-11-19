import json

data = {
    "record1": {
        "values": [1,2,3,4,5],
        "label": "First Thing"
    },
    "record2": {
        "values": [6,7,8,9,10],
        "label": "Second Thing"
    }
}

with open("saveddata.json", "w") as json_file:
    json.dump(data, json_file, indent=2)