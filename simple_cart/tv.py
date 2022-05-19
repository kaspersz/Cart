from products import Product

class TV(Product):
    def __init__(self, name, price, screenSize):
        super().__init__(name, price)
        self.screenSize = screenSize

    def __str__(self):
        return super().__str__() + " " + str(self.screenSize)

