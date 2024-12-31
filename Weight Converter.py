def weight_converter():
    """Converts weight between pounds and kilograms."""
    while True:
        try:
            weight = float(input("What is your weight? "))
            break
        except ValueError:
            print("Invalid input. Weight must be a numeric value.")

    weight_type = input("Enter the unit of weight (lbs or kg): ").strip().lower()
    if weight_type == "lbs":
        converted_weight = weight * 0.45
        print(f"You weigh {converted_weight:.2f} kilograms.")
    elif weight_type == "kg":
        converted_weight = weight / 0.45
        print(f"You weigh {converted_weight:.2f} pounds.")
    else:
        print("Invalid unit. Please enter 'lbs' or 'kg'.")

# Example usage:
if __name__ == "__main__":
    weight_converter()
