from products import *
from phone import *
from tv import *

class Cart:
    def __init__(self):
        self.__productsList = []
        self.__cartValue = 0

    def addProduct(self, product):
        if isinstance(product, Product):
            self.__productsList.append(product)

    def calculateCart(self):
        self.__cartValue = 0
        for products in self.__productsList:
            self.__cartValue += products.price

        return self.__cartValue

    def __str__(self):
        print("Product in the cart are:")
        strData = ""
        for products in self.__productsList:
            strData += "Product is: " + products.name + "" + str(products.price) + "\n"

        return strData