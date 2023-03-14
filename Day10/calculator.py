from logo import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculate(n1, n2, operator):
    operation = {
    "+": add(n1, n2),
    "-": subtract(n1, n2),
    "*": multiply(n1, n2),
    "/": divide(n1, n2)
    }
    return operation[operator]

def calculator():
    print(logo)
    isTrue = False
    n1 = float(input("Enter first number : "))

    while not isTrue:
        operator = input("What operation you want to perform? + - * / : ")
        n2 = float(input("Enter another number : "))
        result = calculate(n1, n2, operator)
        print(f"The result of {n1} {operator} {n2} = {result}")
        
        choice = input("Press y to continue with the previous result and n to start a new calculation : ").lower()
        if (choice == "y"):
            n1 = result
        else:
            isTrue = True
            calculator()

calculator()


