import sys

sys.path.append("..")

from produce.inventory import Inventory

#Inherit Inventory
class Search(Inventory):
    def __init__(self):
        super().__init__()
        self.customer=None
    def set_customer(self,customer):
        self.customer=customer
    def sales(self):
        try:
            if len(self.customer.get_items()) == 0:
                raise existError
            all_price=0
            items=self.customer.get_items()
            for name in items:
                num = int(items[name])
                sale_price=num*self.dict[name].price
                all_price =all_price+ sale_price
            for name in items:
                self.dict[name].sale(items[name])
                self.dict[name].advertise()
            print('Have a nice day!')
            return all_price
        except existError:
            print('there is no items!')
        except:
            print('sth wrong')

    def get_current_price(self):
        all_price = 0
        items = self.customer.get_items()
        for name in items:
            num = int(items[name])
            sale_price = num * self.dict[name].price
            all_price =all_price+ sale_price
        if all_price <= float(self.customer.budget):
            print(f'You have spent {all_price} dollars, and left {float(self.customer.budget)-all_price} dollars.')
            return True,all_price
        else:
            print(f'Total price is {all_price} dollars, over budget for{all_price-float(self.customer.budget)}dollars.')
            return False,all_price
    def fruit_detail(self,name):
        if name in self.dict:
            print(f'fruits {name}, price {self.dict[name].price}, inventory {self.dict[name].inventory}')
            return True
        print("Sorry, we don't have this kind of fruits.")
        return False

