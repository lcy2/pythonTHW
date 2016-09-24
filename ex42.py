## animal is-a object (yes, sort of confusing) look at the extra credit

class Aimal(object):
    pass

## ?is-a
class Dog(Animal)

    def __init__(self, name):
        ## has-a
        self.name = name
        
## ?is-a
class Cat(Animal):

    def __init__(self, name):
        ## ?has-a
        self.name = name

        
class Person(object):
    def __init__(self, name):
    ## has-a
    self.name = name
    
    ## person has-a pet of some kind
    self.pet = None
    
        

## ?? is-a
class Employee(Person):

    def __init__(self, name, salary):
        ## ??has-a
        super(Employee, self).__init__(name)
        ## ?has-a
        self.salary = salary
        
## ?? is-a
class Fish(object)
    pass
    
## ?? is-a
class Salmon(Fish):
    pass
    
## ?? is-a
class Halibut(Fish):
    pass
    
    
## rover is-a Dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

##?? has-a
mary.pet = satan

## has-a
frank.pet = rover

## is-a
flipper = Fish()

## is-a
crouse = Salmon()

## is-a
harry = Halibut()