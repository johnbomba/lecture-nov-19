from app.controller import run
import os

# what's going on here is
# get the file path to the directory containing this python file
# declare the name of our data file
# construct a path that is our base directory joined with our file name

BASE_DIRECTORY = os.path.dirname(__file__)
filename = "tellerdata.json"
filepath = os.path.join(BASE_DIRECTORY, filename)

run(filepath)