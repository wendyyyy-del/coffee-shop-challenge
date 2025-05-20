from coffeeshop import Customer, Coffee, Order

cus1 = Customer("Titus")
cof1 = Coffee("Dormans")
od1 = Order(cus1, cof1, 9.5)

print(od1.customer.name)  
print(od1.coffee.name)    
print(od1.price)
    
