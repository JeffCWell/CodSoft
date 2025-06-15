def calculator():
    print("My Calculator")
    print("Operations: + is Addition, - is Subtraction, * is Multiplication, / is Division")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter operation (+, -, *, /): ")

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Division by zero is not allowed.")
                    continue
            else:
                print("Invalid operation.")
                continue

            print(f"The result is: {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        proceed = input("Do you want to proceed (yes/no): ").lower()
        if proceed != 'yes':
            print("Thank you for using the calculator!")
            break

calculator()
