from app.controller import addtwo
from app import repeatstring
# repeat string is defined in app's __init__.py, things defined in that special file
# act as if they existed in a file called app.py

assert addtwo(5,3) == 8, "addtwo should return the sum of two arguments"

assert repeatstring("Ok ") == "Ok Ok ", "repeatstring concats a string with itself"

from app import addtwo

assert addtwo(7,8) == 15, "second addtwo import also works"

from app import DATABASEPATH