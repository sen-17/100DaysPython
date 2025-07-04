from art import calculator

def add(n1 , n2):
    return n1 + n2

def substract(n1 , n2):
    return n1 - n2

def multiply(n1 , n2):
    return n1 * n2

def division(n1,n2):
    return n2/n1

def modulo(n1,n2):
    return n1 % n2

def input_number(n=None):
    while True:
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulo")

        ask = int(input("What would you like to use? "))

        if n is None:
            n1 = int(input("Input first number: "))
        else:
            n1 = n
            print(f"First number (from previous result): {n1}")

        n2 = int(input("Input second number: "))

        if ask == 1:
            return add(n1 , n2)
        elif ask == 2:
            return substract(n1 , n2)
        elif ask == 3:
            return multiply(n1 , n2)
        elif ask == 4:
            return division(n1 , n2)
        elif ask == 5:
            return modulo(n1 , n2)

def welcome():
    print(calculator)
    print("Welcome to Calculator!")


def main():
    welcome()
    result = input_number()

    while True:
        print(f"Result : {result}")

        ask = input(f"Type 'y' to continue calculating with {result}, or 'n' to start over, or 'q' to quit: ").lower()

        if ask == "y":
            result = input_number(result)
        elif ask == "n":
            result = input_number()
        elif ask == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid input.")


main()


