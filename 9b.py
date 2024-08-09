def handle_exceptions():
    try:
        num = int(input("Enter a number: "))
        print(f"Number: {num}")
        result = 10 / num
        print(f"Division result: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("No exceptions occurred.")
    finally:
        print("Execution completed.")

handle_exceptions()
