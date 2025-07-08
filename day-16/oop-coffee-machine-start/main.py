from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

item = Menu()
machine = CoffeeMaker()
money = MoneyMachine()

while True:
    ask = input(f"Which coffee do you want to buy? {item.get_items()}\n").lower()

    if ask == "latte":
        latte = item.find_drink("latte")
        check = machine.is_resource_sufficient(latte)

        if check:
            latte_cost = latte.cost
            money.make_payment(latte_cost)
            machine.make_coffee(latte)

    elif ask == "cappuccino":
        cappuccino = item.find_drink("cappuccino")
        check = machine.is_resource_sufficient(cappuccino)

        if check:
            cappuccino_cost = cappuccino.cost
            money.make_payment(cappuccino_cost)
            machine.make_coffee(cappuccino)
    
    elif ask == "espresso":
        espresso = item.find_drink("espresso")
        check = machine.is_resource_sufficient(espresso)

        if check:
            espresso_cost = espresso.cost
            money.make_payment(espresso_cost)
            machine.make_coffee(espresso)
            

    elif ask == "report":
        print(machine.report())
        print(money.report())


    












    