def calculator():
    print("Welcome to the Simple Calculator!")
    print("..................................")
    
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator: ")
    num2 = float(input("Enter second number: "))
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2 if num2 != 0 else "Error (Division by zero)"
    else:
        result = "Invalid Operator"
        
    print(f"Result: {result}")

calculator()