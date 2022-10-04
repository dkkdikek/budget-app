

import budget as b
from unittest import main

food =  b.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = b.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = b.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)

print(b.create_spend_chart([food,clothing,auto]))
#print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
#main(module='test_module',exit=False)