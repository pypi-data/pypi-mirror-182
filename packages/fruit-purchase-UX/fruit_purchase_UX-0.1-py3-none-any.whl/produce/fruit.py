class Fruit():
    def __init__(self, name,price,inventory,discount=1):
        self.name=name
        self.price = price
        self.discount = discount
        self.inventory=inventory
        self.expiry=7 
    def get_name(self):
        return self.name

#search price
    def get_price(self):
        print(f'fruit {self.name}, price {self.price}')
        return self.price*self.discount

# search discount
    def get_discount(self):
        print(f'fruit {self.name}, discount {self.discount}')
        return self.discount

#set discount
    def set_discount(self,discount):
        self.discount=discount

#search expiry time
    def get_expiry(self):
        print(f'fruit {self.name}, expire time {self.expiry}')
        return self.expiry

#search inventory
    def get_inventory(self):
        print(f'fruit {self.name}, inventory {self.inventory}')
        return self.inventory

#return price
    def sale(self,num):
        if(self.inventory<=0):
            print("Out of storage.")
            return 0
        if (int(num)>self.inventory):
            print("Out of storage.")
            return 0
        self.inventory=self.inventory-int(num)
        return self.price*int(num)

#five kinds of fruits' information
class Apple(Fruit):
    def __init__(self,price, inventory):
        super().__init__('Apple',price, inventory)
    def advertise(self):
        print("See you next time!")

class Banana(Fruit):
    def __init__(self,price, inventory):
        super().__init__('Banana',price, inventory)
    def advertise(self):
        print("See you next time!")
        
class Pear(Fruit):
    def __init__(self,price, inventory):
        super().__init__('Pear',price, inventory)
    def advertise(self):
        print("See you next time!")

class Orange(Fruit):
    def __init__(self,price, inventory):
        super().__init__('Orange',price, inventory)
    def advertise(self):
        print("See you next time!")

class Grape(Fruit):
    def __init__(self,price, inventory):
        super().__init__('Grape',price, inventory)
    def advertise(self):
        print("See you next time!")