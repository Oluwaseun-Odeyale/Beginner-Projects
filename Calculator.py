import math

class Calculator:
    """
    A simple calculator class to perform arithmetic operations between two numbers.
    Supported operations: +, -, *, /, ^ (power), ~ (square root of the product).
    """

    def arithmetic_operator(self):
        print("Calculator App for Two Numbers")
        print("=================================")

        # Input first number with error handling
        while True:
            try:
                num1 = float(input("Enter the first number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Input operator
        valid_operators = ["+", "-", "/", "*", "^", "~"]
        while True:
            operator = input("Enter operator (+, -, /, *, ^, ~): ").strip()
            if operator in valid_operators:
                break
            else:
                print("Invalid operator. Please choose from +, -, /, *, ^, ~.")

        # Input second number with error handling (not required for square root operation)
        if operator != "~":
            while True:
                try:
                    num2 = float(input("Enter the second number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        # Perform the operation
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "/":
            if num2 == 0:
                print("Division by zero is not allowed.")
                return
            result = num1 / num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "^":
            result = num1 ** num2
        elif operator == "~":
            result = math.sqrt(num1)
        else:
            print("An unexpected error occurred.")
            return

        # Display the result
        print(f"The result of {num1} {operator} {num2 if operator != '~' else ''} is: {result}")

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    calc.arithmetic_operator()
