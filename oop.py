class Car:

    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

    def show(self):
        print(f"My dream car is {self.make} and "
              f"my model is {self.model} manufactured in {self.year} and the colour is {self.colour}")


myobj = Car("Toyota", "Vitz", 2020, "pink")
myobj.show()
myobj2 = Car("Mazda", "CX5", 2018, "black")
myobj2.show()
