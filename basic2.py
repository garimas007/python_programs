# Inheritance and Polymorphism
# base class Animal- name, speak() - print "animal sound"
# derived class Dog - speak() - "woof!"
# derived class Cat - speak() - "meow"
# object dog and cat - speak()

class Animal:                        #base class
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("This Animal sounds like - ")

class Dog(Animal):                   #derived class
    def speak(self):
        print("Woof!")

class Cat(Animal):                   #derived class
    def speak(self):
        print("Meow!")

odog = Dog(name='Bruno')
ocat = Cat(name='Blackie')

odog.speak()
ocat.speak()