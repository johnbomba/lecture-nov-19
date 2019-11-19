from firstclass import Person

billy = Person()  # creating an *instance* of the class Person

# a class is a blueprint for creating an object
# an object is said to be an 'instance' of a class

billy.sayhi()

billy.name = "Miguel"

billy.sayhi()

joe = Person("Joe")

assert isinstance(joe, Person)
# reminder: assert takes 1 or 2 arguments, the first is a True / False boolean expression
# the second is an optional message. assert does nothing it the boolean is True
# if the boolean is False, it will raise an AssertionError and display the message
#
# assert is NOT for implementing features, it is for testing and verifying that
# your code works the way you think it does.

# testing inherit

from inheritclass import Employee

max = Employee()
max.sayhi()  # defined in Person

assert isinstance(max, Employee)
assert isinstance(max, Person)  # an object of a class is also an instance of any class
# its class inherits from. Because Employee is a type of Person, max is also an instance
# of Person
assert isinstance(12, int)

max.sayjob()  # defined in Employee
