#Abstract Classes
#6/3/24

class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Method 'speak' not implemented in subclass!")

class Tiger(Cat):
    def speak(self):
        return("ROAR!")

class Kitten(Cat):
    def play(self):
        return("Tired kitty!")

t = Tiger("Tony")
k = Kitten("Nemal")
print(t.speak())
print(k.speak())

#error will only occur if the child class doesnt have said method (in this case it is speak)
#error will happen becuase tiger does not have speak method

# --------------------------------------------------------


import abc #abc = Abstract Base Class

class Cat(metaclass = abc.ABCMeta):
    def __init__(self, name):
        self.name = name
    @abc.abstractmethod
    def speak(self):
        pass 

class Tiger(Cat):
    def speak(self):
        return("ROAR!")

class Kitten(Cat):
    def play(self):
        return("Tired kitty!")

t = Tiger("Tony")
k = Kitten("Nemal")
print(t.speak())
print(k.speak())


---------------------------------------------------------


import abc #abc = Abstract Base Class

class Cat(metaclass = abc.ABCMeta):
    def __init__(self, name):
        self.name = name
    @abc.abstractmethod
    def speak(self):
        pass 

class Tiger(Cat):
    def speak(self):
        return("ROAR!")

class Kitten(Cat):
    def play(self):
        return("Tired kitty!")

t = Tiger("Tony")
k = Kitten("Nemal")
print(t.speak())
print(k.speak())

#abc is a library that contains templates for doing abstraction and such
#ABCMeta is the parent class of all abstrac classes
#@abc.abstractmethod tags a method as being abstract

---------------------------------------------------------


import abc #abc = Abstract Base Class

class Cat(metaclass = abc.ABCMeta):
    def __init__(self, name):
        self.name = name
    @abc.abstractmethod
    def speak(self):
        pass 

class Tiger(Cat):
    def speak(self):
        return("ROAR!")

class Kitten(Cat):
    def play(self):
        return("Tired kitty!")

t = Tiger("Tony")
k = Kitten("Nemal")
print(t.speak())
print(k.speak())


# A concrete class is a class you can instantiate (make an object out of).
#Every child class refers to parent class



