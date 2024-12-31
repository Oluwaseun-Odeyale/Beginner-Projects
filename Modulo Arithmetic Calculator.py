def modulo_arithmetics_calculator():
    """
    Calculates (number^power) % mod efficiently.
    Uses Python's built-in modular exponentiation for optimal performance.
    """
    print("Modulo Arithmetic Calculator\n")
    try:
        number = int(input("Enter the base number: "))
        power = int(input("Enter the power: "))
        mod = int(input("Enter the modulus: "))
    except ValueError:
        print("Invalid input! Please enter valid integers for all values.")
        return

    # Compute the result using modular exponentiation
    result = pow(number, power, mod)
    print(f"Result: ({number}^{power}) % {mod} = {result}")


# Example usage:
if __name__ == "__main__":
    modulo_arithmetics_calculator()
