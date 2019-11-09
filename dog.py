class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        if self.weight > 29:
            print(self.name, 'says "WOOF WOOF"')
        else:
            print(self.name, 'says "woof woof"')

    def human_years(self):
        return 7 * self.age

    def walk(self):
        print(self.name, 'is walking')
    
    def __str__(self):
        return "I'm a dog named " + self.name

def print_dog(dog):
    print(dog.name + "'s", 'age is', dog.age,
            'and weight is', dog.weight)

class ServieceDog(Dog):
    def __init__(self, name, age, weight, handler):
        Dog.__init__(self, name, age, weight)
        self.hanlder = handler
        self.is_working = False
    
    def walk(self):
        if self.is_working:
            print(self.name, 'is helping its handler', self.hanlder, 'walk')
        else:
            Dog.walk(self)

    def bark(self):
        if self.is_working:
            print(self.name, 'says, "I can\'t bark, I\'m working')
        else:
            Dog.bark(self)

class Frisbee:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "I'm a " + self.color + ' frisbee'

class FrisbeeDog(Dog):
    def __init__(self, name, age, weight):
        Dog.__init__(self, name, age, weight)
        self.frisbee = None

    def bark(self):
        if self.frisbee:
            print("I can't bark, I have a frisbee in my mouth.")
        else:
            Dog.bark(self)

    def walk(self):
        if self.frisbee:
            print("I can't walk")
        else:
            Dog.walk(self)

    def catch(self, frisbee):
        self.frisbee = frisbee
        print(self.name, 'caught', frisbee.color, 'frisbee.')

    def give(self):
        if self.frisbee:
            frisbee = self.frisbee
            self.frisbee = None
            print('Give the frisbee')
            return frisbee
        else:
            print('Have no frisbee')
            return None

    def __str__(self):
        msg = "I'm a dog named " + self.name
        if self.frisbee:
            msg += ' and I have a frisbee'
        return msg

class Hotel:
    def __init__(self, name):
        self.name = name
        # self.kernel_names = []
        # self.kernel_dogs = []
        self.kernel = {}

    def check_in(self, dog):
        if isinstance(dog, Dog):
            # self.kernel_names.append(dog.name)
            # self.kernel_dogs.append(dog)
            self.kernel[dog.name] = dog
            print(dog.name, 'check in')
        else:
            print('Sorry, only dogs are allowed into')
    
    def check_out(self, name):
        # for i in range(0, len(self.kernel_names)):
        #     if name == self.kernel_names[i]:
        #         dog = self.kernel_dogs[i]
        #         del self.kernel_names[i]
        #         del self.kernel_dogs[i]
        #         print(dog.name + 'ckecked out')
        #         return dog
        if name in self.kernel:
            dog = self.kernel[name]
            print(dog.name + ' ckecked out')
            del self.kernel[name]
            return dog

        print('Sorry,', name, ' is not boarding at', self.name)
        return None
    
    def barktime(self):
        for dog_name in self.kernel:
            dog = self.kernel[dog_name]
            dog.bark()

    # def walking_service(self):
    #     for dog_name in self.kernel:
    #         dog = self.kernel[dog_name]
    #         dog.walk()

    def hire_walker(self, walker):
        if isinstance(walker, DogWalker):
            self.walker = walker
        else:
            print('Sorry,', walker.name, ' is not a Dog Walker')
        
    def walking_service(self):
        if self.walker:
            self.walker.walk_the_dogs(self.kernel)

class Cat:
    def __init__(self, name):
        self.name = name
    
    def meow(self):
        print(self.name, 'Says, Meow')

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "I'm a person and my name is " + self.name

class DogWalker(Person):
    def __init__(self, name):
        Person.__init__(self, name)

    def walk_the_dogs(self, dogs):
        for dog_name in dogs:
            dogs[dog_name].walk()

def test_code():
    # codie = Dog('Codie', 12, 38)
    # jackson = Dog('Jackson', 9, 12)
    # #print_dog(codie)
    # #print_dog(jackson)
    # print(codie.name + "'s age in human years is ", codie.human_years())
    # print(jackson.name + "'s age in human years is ", jackson.human_years())
    # dude = FrisbeeDog('Dude', 5, 20)
    # blue_frisbee = Frisbee('blue')
    # print(dude)
    # dude.bark()
    # dude.catch(blue_frisbee)
    # dude.bark()
    # print(dude)
    # frisbee = dude.give()
    # print(frisbee)
    # print(dude)
    codie = Dog('Codie', 12, 38)
    jackson = Dog('Jackson', 9, 12)
    sparky = Dog('Sparky', 2, 14)
    rody = ServieceDog('Rody', 8, 38, 'Joseph')
    rody.is_working = True
    frisbee = Frisbee('red')
    dude = FrisbeeDog('Dude', 5, 20)
    # dude.catch(frisbee)
    # kitty = Cat('Kitty')
    

    hotel = Hotel('Doggie Hotel')
    hotel.check_in(codie)
    hotel.check_in(jackson)
    hotel.check_in(rody)
    hotel.check_in(dude)
    # hotel.check_in(kitty)

    # dog = hotel.check_out(codie.name)
    # print('Checked out', dog.name, 'who is', dog.age, 'and', dog.weight, 'lbs')
    # dog = hotel.check_out(jackson.name)
    # print('Checked out', dog.name, 'who is', dog.age, 'and', dog.weight, 'lbs')
    # dog = hotel.check_out(rody.name)
    # print('Checked out', dog.name, 'who is', dog.age, 'and', dog.weight, 'lbs')
    # dog = hotel.check_out(dude.name)
    # print('Checked out', dog.name, 'who is', dog.age, 'and', dog.weight, 'lbs')
    # dog = hotel.check_out(sparky.name)
    # print('Checked out', dog.name, 'who is', dog.age, 'and', dog.weight, 'lbs')
    
    # hotel.barktime()

    # codie.walk()
    # jackson.walk()
    # rody.walk()
    # dude.walk()

    joe = DogWalker('joe')
    hotel.hire_walker(joe)
    hotel.walking_service()

test_code()