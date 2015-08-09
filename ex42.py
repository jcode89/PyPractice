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

    def __init__(self, name, age=0, height="", outgoing=None):
        ## Person has-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None
        self.age = age
        self.height = height
        self.outgoing = outgoing

    def print_name(self):
        print self.name

    def features(self):
        ToF = {"age": self.age, "height": self.height, "personality": self.outgoing}
        return ToF


## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary, age, height, outgoing):
        ## ?? hmm what is this strange magic?
        ## Employee has-a name
        super(Employee, self).__init__(name, age, height, outgoing)
        ## Employee has-a salary
        self.salary = salary
        super(Employee, self).print_name()
        super(Employee, self).features()


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

'''I have added in a dictionary for the Person class, but **kwargs
probably could have been used.'''

## Rover is-a Dog
rover = Dog("Rover")
rover.hairy()
## Satan is-a Cat
satan = Cat("Satan")
satan.has_hair()
## Mary is-a Person
mary = Person("Mary", 26, "5Ft 4in", True)
mary.print_name()
print "Mary's age is %r, her height is %r." % (mary.features()['age'], mary.features()['height'])
if mary.features()['personality']:
    print "Mary is very outgoing!"
## Mary has-a pet and her pet is-a cat and her cat has-a name
mary.pet = satan
mary.pet.has_hair()
## frank is-a Employee
frank = Employee("Frank", 120000, 36, "6ft", False)
frank.print_name
print "Frank makes %d" % frank.salary
print "Frank is %d years old and is %s tall." % (frank.features()['age'], frank.features()['height'])
if not frank.features()['personality']:
    print "Frank is not very outgoing!"
## Frank has-a pet, his pet is-a dog, his dog has-a name
frank.pet = rover
frank.pet.hairy()
## flipper is-a Fish
flipper = Fish("grey", "black", "super long")
flipper.features()
## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
# barry is a dictionary and each key in the dictionary is a class
barry ={"Fish": Fish("Yellow", "Green", "Puffy"), "Animal": Animal("Puffer Fish", False)}
## I did not realize I used features as a method in two seperate classes.
barry["Fish"].features()
barry["Animal"].features()

# barry could also be a list
barry = [Fish("Yellow", "Green", "Puffy"), Animal("Puffer Fish", False)]
barry[1].features()
barry[0].features()
