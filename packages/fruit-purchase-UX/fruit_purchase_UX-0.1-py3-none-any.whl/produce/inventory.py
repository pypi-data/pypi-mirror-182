import sys

sys.path.append("..")

from produce.fruit import Apple, Banana, Pear, Orange, Grape

class Inventory():
    def __init__(self):
#fruits information initialization
        self.dict={}
        apple=Apple(15,21)
        apple.set_discount(0.7)
        banana = Banana(10, 21)
        banana.set_discount(0.8)
        pear = Pear(20, 21)
        pear.set_discount(0.9)
        orange = Orange(8, 21)
        grape = Grape(6, 21)
        self.dict[apple.get_name()]=apple
        self.dict[banana.get_name()] = banana
        self.dict[pear.get_name()] = pear
        self.dict[orange.get_name()] = orange
        self.dict[grape.get_name()] = grape
        
#search inventory
    def get_inventory(self):
        try:
            for key in self.dict:
                self.dict[key].get_inventory()
        except:
            print('sth wrong')
        else:
            return self.dict


#query the price of fruit according to the name of the fruit
    def get_price(self,name):
        try:
            if name in self.dict:
                return self.dict[name].get_price()
            else:
                print("Sorry, we don't have this kind of fruit.")
        except:
            print('sth wrong')

#search discount according to fruits' name
    def get_discount(self,name):
        try:
            if name in self.dict:
                return self.dict[name].get_discount()
            else:
                print("Sorry, we don't have this kind of fruit.")
        except:
            print('sth wrong')
# query all inventory and sort by price
    def get_sort_price(self):
        try:
            d_order = sorted(self.dict.items(), key=lambda x:x[1].price, reverse=False)
        except:
            print('sth wrong')
        else:
            for key in d_order:
                print(f'fruit {key[1].name}, inventory {key[1].inventory}, price {key[1].price}')
            return self.dict

    def get_expiry(self):
        for key in self.dict:
            self.dict[key].get_expiry()
        return self.dict
