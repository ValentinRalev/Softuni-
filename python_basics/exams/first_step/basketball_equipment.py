annual_tax = int(input())
basket_shoes = annual_tax * 0.60
basket_equip = basket_shoes * 0.80
basketball = basket_equip * 0.25
basket_acces = basketball * 0.20
all_cost = basket_acces + basket_equip + basket_shoes + basketball + annual_tax
print(all_cost)