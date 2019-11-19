# things defined in dunder init are importable directly from app (the name of the
# folder defining the module/package) instead of app.filename

def repeatstring(string):
    return string + string

from app.controller import addtwo 

DATABASEPATH = "./data/mydata.db"

# defined in another file, but will exist as if
# defined just in app instead of app.controller