class Fruits():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"My favourite fruit is {self.name} and it costs Ksh.{self.price}")


myobj = Fruits("Mango", 50)
myobj.display()
myobj2 = Fruits("Melon", 50)
myobj2.display()
myobj3 = Fruits("Pineapple", 30)
myobj3.display()
myobj4 = Fruits("Oranges", 40)
myobj4.display()
myobj5 = Fruits("Apple", 35)
myobj5.display()
