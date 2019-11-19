
class Person:

    def __init__(self, name=None):
        # defines what happens when I say newobject = Person()
        # self.name = "Billy"
        if name == None:
            self.name = "Nobody"
        else:
            self.name = name

        # 'properties' of self stick around after objects are created and
        # methods are called so values in self.property set by one method
        # can be seen by others

    def sayhi(self):
        print(f"hi, my name is {self.name}")