from app.view import sayhello 

# note that I don't say from view import say hello
# even though these files are in the same directory, you still have to import
# as if you were in the base directory, because main.py is the file that will be
# directly run

def run():
    sayhello()

def addtwo(x, y):
    return x + y

if __name__ == "__main__":
    run()