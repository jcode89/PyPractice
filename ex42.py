## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):

    def __init__(self, _type, hair=None):
        self.hair = hair
        self.type = _type

    def features(self):
        print "I am a ", self.type
        if self.hair == True:
            print "I have hair!"
        else:
            print "Hairless animal."

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name
        super(Dog, self).__init__("Dog", True)
    def hairy(self):
        ## calls the method from the Animal class
        super(Dog, self).features()

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name
        super(Cat, self).__init__("Cat", False)

    def has_hair(self):
        super(Cat, self).features()

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

    def print_name(self):
        print self.name


## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        ## Employee has-a name
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary
        super(Employee, self).print_name()



## Fish is-a object
class Fish(object):

    def __init__(self, skin, eyes, body):
        self.skin = skin
        self.eyes = eyes
        self.body = body

    def features(self):
        print"I have {} skin, {} eyes, and a {} body".format(self.skin,
                                                            self.eyes,
                                                            self.body)

## Salmon is-a Fish
class Salmon(Fish):
    def __init__(self):
        super(Salmon, self).__init__("red", "green", "very long")
        super(Salmon, self).features()

## Halibut is-a Fish
class Halibut(Fish):
    def __init__(self):
        super(Halibut, self).__init__("brown", "yellow", "medium")
        super(Halibut, self).features()

'''This exercise is almost finished. The next step is to make new
relationships that are either lists or dictionaries.'''

## Rover is-a Dog
rover = Dog("Rover")
rover.hairy()
## Satan is-a Cat
satan = Cat("Satan")
satan.has_hair()
## Mary is-a Person
mary = Person("Mary")
mary.print_name()
## Mary has-a pet and her pet is-a cat and her cat has-a name
mary.pet = satan
mary.pet.has_hair()
## frank is-a Employee
frank = Employee("Frank", 120000)
frank.print_name
## Frank has-a pet, his pet is-a dog, his dog has-a name
frank.pet = rover

## flipper is-a Fish
flipper = Fish("grey", "black", "super long")
flipper.features()
## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
