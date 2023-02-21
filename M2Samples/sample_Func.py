def myFunc(val, name = "world"):
    print(f"Hello, name:{name} val:{val}")


myFunc("matt", "matt")

def find_prime(num):
    pass
#pass fills in the body but doesn't do anything yet


#the parameter with * which will turn the input into a tuple
def grace(*star):
    print(star)

grace("hi", "bye")


#not sure how this works

"""
def grace2(**star):
    print()

grace2()


"""


class Person:
    name = "Bob"
    age = 50
    job = "Painter"

    def __init__(self) -> None:
        #self is the object refernce
        self.name = "Matt"
        self.age = 32
        self.job = "Lecturer"

    def __repr__(self) -> str:
        return str(self.__dict__)


person = Person()
print(f"{person}")
#his dict prints mre info then mine?


#dictionary = key value pairs