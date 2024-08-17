def calculator():
    num1 = int(input("Enter the first number: "))

    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter the operation (+, -, *, /): ")

    num2 = int(input("Enter the second number: "))

    if operation == '+':
        result = num1 + num2
        print(num1 ,"+", num2 ,"=", result)
    elif operation == '-':
        result = num1 - num2
        print(num1 ,"-", num2 ,"=", result)
    elif operation == '*':
        result = num1 * num2
        print(num1 ,"*", num2 ,"=", result)
    elif operation == '/':
        if num2 != 0:
            result = num1 // num2
            print(num1 ,"/", num2 ,"=", result)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")
        
calculator()
