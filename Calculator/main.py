try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("What kind of operation do you want to perform. Press + for addition\n - for subtration\n * for mupltiplication\n / for division")

    o = input("Enter the operation: ")
    match o:
        case "+":
            print(f"The result is: {a+b}")
        case "-":
            print(f"The result is: {a-b}")
        case "*":
            print(f"The result is: {a*b}")
        case "/":
            print(f"The result is: {a/b}")
        case _:
            print(f"There was an error. Pls try again.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except ValueError:
    print("Invalid input. Please enter numeric values.")

except Exception as e:
    print("Enter a valid value of a and b.")
