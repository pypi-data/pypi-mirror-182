class Customer():
#Initialization
    def __init__(self):
        self.budget=0
        self.items={}
        
#set budget
    def set_budget(self,budget):
        self.budget=budget

#prevent duplicate entry
    def shop_item(self,name,num):
        if name in self.items:
            print('Please do not enter the same fruit.')
            return
        self.items[name]=num
 
# purchase list  
    def items_detail(self):
        print('Purchase List：')
        try:
            if not self.items:
                raise ValueError("no items")
            for name in self.items:
                print(f' {name},{self.items[name]}')
        except ValueError as ex:
            print(ex)
        except:
            print(ex)

# store-purchased fruits 
    def get_items(self):
        return self.items
  
#clear purchase list
    def clear_items(self):
        print('Please re-select the fruit you want to buy.')
        self.items={}




