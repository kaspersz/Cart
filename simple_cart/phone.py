from products import Product

class Phone(Product):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.color = color

    def __str__(self):
        return super().__str__() + " " + str(self.color)