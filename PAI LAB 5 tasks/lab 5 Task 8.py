try:
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integer numbers.")
except Exception as e:
    print("An unexpected error occurred:", e)
