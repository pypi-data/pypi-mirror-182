# Fruits Purchase System 
## Group 10 
## Xiaoxiao Fu & Ujjwal Upadhyay

[![Build Status](https://app.travis-ci.com/ujjwal-upadhyay/DATA533_Project_Group_10_Step3.svg?branch=main)](https://app.travis-ci.com/ujjwal-upadhyay/DATA533_Project_Group_10_Step3)

### 1. Description of the package
Our project topic is Fruits Purchase System. We create two sub-packages named as customer and produce. The main modules in these sub-packages are Customer.py, which manages customers’ purchasing needs. Search.py is used for customers to search for fruits’ storage, price, and notification words. Fruits.py is used to set different fruits' information, like price, discount, inventory and expiry time. Inventory.py are used for record the fruits’ inventory information.

### 2. Description of the functions
#### (1) Functions in Customer.py
* set_budget() : This functions helps customers to enter their budgets.
* shop_item(): This function prevent duplicate entry. If customers enter the same fruits, the systerm will notice that "Please do not enter the same fruit."
* items_detail(): This function shows purchase list.
* get_items(): This function clears purchase list according to the users' choice.
#### (2) Functions in Search.py
* set_customer() - This function helps to intialize the customer in search class.
* sales() - This function helps to calculate the total amount of the items purchased by the customer.
* get_current_price() - This function helps to get the current amount of shopping customer has done.
* fruit_detail() - This function provides the list of fruits.
#### (3) Functions in Fruit.py
* get_name() - This function will return the name of the fruit.
* get_price() - This function will return the discounted price of the fruit.
* get_discount() - This function will return the discount for the given fruit.
* set_discount() - This function will set the discount for the fruit.
* get_expiry() - This function will setup the expiry default date i.e 7 for each fruit.
* get_inventory() - This function will initialize the entire inventory.
* sale() - This function will update the inventory and return the total price of the item.

#### (4) Functions in Inventory.py
* get_inventory() - This function will display the list of entire inventory.
* get_price() - This function will return the price of the fruit from the inventory.
* get_discount() - This function will return the discount price of the fruit from the inventory.
* get_sort_price() - This function will return the sorted list of the items purchased by the customer.
* get_expiry() - This function will call the Fruit module method and display the expiry dates for given fruit.

#### Description vedio link: https://youtu.be/afHm1F9GPmU
