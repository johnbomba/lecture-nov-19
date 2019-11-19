from firstclass import Person

# note: you CAN inherit from multpile parent classes with class Child(Parent1, Parent2)
# there are rules for whiche methods override which, but the truth is is this is
# very seldomly used. But you may want to read up on "multiple inheritance"

class Employee(Person): # The Employee class is a type of Person class
    
    def __init__(self, name=None, title=None):
        # if name is None:
        #     self.name = "Nobody"
        # else:
        #     self.name = name
        super().__init__(name)  
        # run self through the parent class's __init__ passing
        # the name argument given here to it

        # super() gives you your self object as if it were an instance of the
        # parent class. you can use it to call a parent's version of a method
        # inside of a new version of that method
        
        if title is None:
            self.title = "Unemployed"
        else:
            self.title = title
    
    def sayjob(self):
        print(f"Hello, my name is {self.name} and my job is {self.title}.")