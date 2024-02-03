#Adding products
#Calculating the total value of the inventory
#Handling discounted products

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def totalValue(self):
        return self.quantity * self.price

class Disscountprod(Product):
    def __init__(self, name, price, quantity, discount):
        super().__init__(name, price, quantity)
        self.discount = discount

    def totalValue(self):
        discounted_price = self.price - (self.price * self.discount / 100 )
        return discounted_price * self.quantity

prod1 = Product("item1", 10 , 5)
prod2 = Disscountprod("item2", 100, 5, 10)

totalValue1 = prod1.totalValue()
totalValue2 = prod2.totalValue()

print(totalValue1)
print(totalValue2)