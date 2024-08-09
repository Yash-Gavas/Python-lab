def arithmetic_operations():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Choose operation: 1-Add, 2-Subtract, 3-Multiply, 4-Divide")
    choice = int(input("Enter choice: "))

    if choice == 1:
        print(f"Result: {num1 + num2}")
    elif choice == 2:
        print(f"Result: {num1 - num2}")
    elif choice == 3:
        print(f"Result: {num1 * num2}")
    elif choice == 4:
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid choice")

arithmetic_operations()
