from menu import coffee_menu , resources
from art import logo

def get_coffee():
    print("""
    ╔════════════════════════════════════╗
    ║           ☕ COFFEE MENU ☕        ║
    ╠════════════════════════════════════╣
    ║  1. Cappuccino     - ${:.2f}         ║
    ║  2. Latte          - ${:.2f}         ║
    ║  3. Espresso       - ${:.2f}         ║
    ╠════════════════════════════════════╣
    ║  Type 'report' to view resources   ║
    ║  Type 'off' to shut down machine   ║
    ║  Type 'restock' to restock machine ║
    ╚════════════════════════════════════╝
    """.format(
    coffee_menu["cappuccino"]["cost"],
    coffee_menu["latte"]["cost"],
    coffee_menu["espresso"]["cost"]
    ))

    return input("➡ What would you like to order? ").lower()

def report_resources():
    water = resources["water"]
    milk = resources ["milk"]
    coffee = resources["coffee"]

    return water , milk , coffee

def maintainance():
    return f"Shutting down machine..."

def cappuccino():
    water = coffee_menu["cappuccino"]["ingredients"]["water"]
    coffee = coffee_menu["cappuccino"]["ingredients"]["coffee"]
    milk = coffee_menu["cappuccino"]["ingredients"]["milk"]

    return water , coffee , milk

def espresso():
    water = coffee_menu["espresso"]["ingredients"]["water"]
    coffee = coffee_menu["espresso"]["ingredients"]["coffee"]
    
    return water, coffee 

def latte():
    water = coffee_menu["latte"]["ingredients"]["water"]
    coffee = coffee_menu["latte"]["ingredients"]["coffee"]
    milk = coffee_menu["latte"]["ingredients"]["milk"]
    
    return water , coffee , milk

def check_resources(coffee):
    current_water , current_coffee, current_milk = report_resources()

    if coffee == "cappuccino":
        cappuccino_water , cappuccino_coffee , cappuccino_milk = cappuccino()

        if current_water > cappuccino_water and current_coffee > cappuccino_coffee and current_milk > cappuccino_milk:
            q , mq = quarters()
            d , md = dimes()
            n , mn = nickles()
            p , mp = pennies()

            result = pay(coffee , q , d , n , p , mq , md , mn , mp)
            
            if result:
                print("💵 Payment Successful")
                print(f"🍵 Here is your {coffee} coffee")
                deduct_resource(coffee)
            elif type(result) == tuple and result[0] == True:
                print(f"💵 Payment Successful")
                print(f"🪙 Here's your change: {result[1]}")
                print(f"🍵 Here's your {coffee} coffee")
                deduct_resource(coffee)
            else:
                print("Money isnt sufficient. Returning money...")
        else:
            return f"Resources aren't sufficient"
    
    elif coffee == "latte":
        latte_water , latte_coffee , latte_milk = latte()

        if current_water > latte_water and current_coffee > latte_coffee and current_milk > latte_milk:
            q , mq = quarters()
            d , md = dimes()
            n , mn = nickles()
            p , mp = pennies()

            result = pay(coffee , q , d , n , p , mq , md , mn , mp)

            if result:
                print("💵 Payment Successful")
                print(f"🍵 Here is your {coffee} coffee")
                deduct_resource(coffee)
            elif type(result) == tuple and result[0] == True:
                print(f"💵 Payment Successful")
                print(f"🪙 Here's your change: {result[1]}")
                print(f"🍵 Here's your {coffee} coffee")
                deduct_resource(coffee)
            else:
                print("Money isnt sufficient. Returning money...")
        else:
            return f"Resources aren't sufficient"
    
    elif coffee == "espresso":
        espresso_water , espresso_coffee = espresso()

        if current_water > espresso_water and current_coffee > espresso_coffee :
            q , mq = quarters()
            d , md = dimes()
            n , mn = nickles()
            p , mp = pennies()

            result = pay(coffee , q , d , n , p , mq , md , mn , mp)
            
            if result:
                print("💵 Payment Successful")
                print(f"🍵 Here is your {coffee} coffee")
                deduct_resource(coffee)
            elif type(result) == tuple and result[0] == True:
                print(f"💵 Payment Successful")
                print(f"🪙 Here's your change: {result[1]}")
                print(f"🍵 Here's your {coffee} coffee")
                deduct_resource(coffee)
            else:
                print("Money isnt sufficient. Returning money...")
        else:
            return f"Resources aren't sufficient"



def pay(coffee, quarter , dimes , nickles , pennies, many_quarters , many_dimes, many_nickles , many_pennies):
    price = 0
    if coffee == "cappuccino":
        price += coffee_menu["cappuccino"]["cost"]
    elif coffee == "latte":
        price += coffee_menu["latte"]["cost"]
    elif coffee =="espresso":
        price += coffee_menu["espresso"]["cost"]

    total = quarter * many_quarters + dimes * many_dimes + nickles * many_nickles + pennies * many_pennies


    if total == price:
        return True
    elif total > price:
        change = total - price
        return True , change
    else:
        return False

def quarters():
    quarter = 0.25
    many_quarters = int(input("How many quarters? "))
    return quarter , many_quarters

def dimes():
    dimes = 0.10
    many_dimes = int(input("How many dimes? "))
    return dimes , many_dimes

def nickles():
    nickles = 0.05
    many_nickles = int(input("How many nickles? "))
    return nickles , many_nickles

def pennies():
    pennies = 0.01
    many_pennies = int(input("How many pennies? "))
    return pennies , many_pennies

def deduct_resource(coffee_type):
    if coffee_type == "cappuccino":
        water , coffee , milk = cappuccino()
        resources["milk"] -= milk
        resources["water"] -= water
        resources["coffee"] -= coffee
    elif coffee_type == "latte":
        water , coffee , milk = latte()
        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee
    else:
        water, coffee = espresso()
        resources["water"] -= water
        resources["coffee"] -= coffee

def restock():
    try:
        water = int(input("How much water do you want to add? "))
        milk = int(input("How much milk do you want to add? "))
        coffee = int(input("How much coffee do you want to add? "))

        resources["water"] += water
        resources["milk"] += milk
        resources["coffee"] += coffee

        print(f"Succesfully added Water: {water}ml\nMilk: {milk} ml\nCoffee: {coffee} gr")

    except ValueError:
        print("Input a valid integer.")


def main():
    print(logo)
    is_on = True

    while is_on:
        choice = get_coffee()

        if choice == "off":
            is_on = False
        elif choice == "restock":
            restock()
        elif choice == "report":
            water , milk , coffee = report_resources()
            print(f"Water: {water} ml")
            print(f"Milk: {milk} ml")
            print(f"Coffee: {coffee} gr")
        elif choice in ["cappuccino" , "espresso" , "latte"]:
            result = check_resources(choice)

            if result:
                print(result)
        else:
            print("Please enter a valid input.")

if __name__ == "__main__":
    main()
        






    


    




        







