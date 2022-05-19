from cart import *

nokiaPhone = Phone("Nokia", 1000, "Blue")

print(nokiaPhone)

samsungTv = TV("Samsung", 2000, "Black")

print(samsungTv)

cart1 = Cart()

cart1.addProduct(nokiaPhone)
cart1.addProduct(samsungTv)
print(cart1)
print(cart1.calculateCart())