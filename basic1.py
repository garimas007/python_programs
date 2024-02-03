# creating class and object
# car - make, model, year
# methods - start_engine - msg print "car's engine has started"
# object my_car - make(Toyota), model(Camry), year(2022)
# print my_car attributes
# start_engine on my_car

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start_engine(self):
        print("Car's engine has started.")
my_car = Car(make='Toyota', model='Camry', year='2022')
print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.start_engine()