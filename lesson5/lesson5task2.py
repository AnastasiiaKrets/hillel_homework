while True:
    number1 = int(input("Enter a first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    number2 = int(input("Enter a second number: "))

    if operation == "+":
        result = number1 + number2
        print("Result:", result)
    elif operation == "-":
        result = number1 - number2
        print("Result:", result)
    elif operation == "*":
        result = number1 * number2
        print("Result:", result)
    elif operation == "/":
        if number2 != 0:
            result = number1 / number2
            print("Result:", result)
        else:
            print("Error: cannot divide by zero")
    else:
        print("Unknown operation")

    cont = input("Do you want continue? (y/yes to continue): ").lower()
    if cont not in ("y", "yes"):
        print("Calculator stopped.")
        break