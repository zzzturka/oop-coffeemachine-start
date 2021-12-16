from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
state = True
profit = 0
coffee = Menu()
money = MoneyMachine()
maintenance = CoffeeMaker()

# print(coffee.menu[0].ingredients["milk"])
# print(getattr(Menu(), milk)
while state:
    choice = input(f"What would you like? {coffee.get_items()}:  ").lower()
    if choice in coffee.get_items():
        if maintenance.is_resource_sufficient(coffee.find_drink(choice)):
            if money.make_payment(coffee.find_drink(choice).cost):
                maintenance.make_coffee(coffee.find_drink(choice))
        else:
            break
    elif choice == "off":
        state = False
    elif choice == "report":
        maintenance.report()
        money.report()
print("thanks for using our coffee machine!")










