# User Information Class

class Information:
    """
    A class to collect and display user information in a structured format.
    Methods:
        - my_information1: Collects comprehensive user details and displays them.
        - my_information2: Collects and displays basic user details.
    """

    @staticmethod
    def get_positive_integer(prompt):
        """Helper function to get a valid positive integer input."""
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def my_information1(self):
        """Collects and displays detailed user information."""
        name = input("What is your full name? ").title()
        date_of_birth = self.get_positive_integer("What year were you born? ")
        age = 2023 - date_of_birth
        school = input("What school do you attend? ").title()
        favorite_color = input("What is your favorite color? ").title()
        favorite_food = input("What is your favorite food? ").title()
        class_name = input("What is your current class? ").title()
        phone_number = input("What is your phone number? (optional) ")
        email = input("What is your email address? (optional) ")
        address = input("Where do you live (state and country)? ").title()
        birth_place = input("Where were you born (state and country)? ").title()

        print("\n" + " My Information ".center(60, "="))
        print(f"1. My name is {name}")
        print(f"2. I am {age} years old")
        print(f"3. I attend {school}")
        print(f"4. My favorite color is {favorite_color}")
        print(f"5. My favorite food is {favorite_food}")
        print(f"6. I am in {class_name}")
        print(f"7. My phone number is {phone_number}")
        print(f"8. My email address is {email}")
        print(f"9. I live in {address}")
        print(f"10. I was born in {birth_place}")

    def my_information2(self):
        """Collects and displays basic user information."""
        name = input("What is your full name? ").title()
        age = self.get_positive_integer("What is your age? ")
        school = input("What is the name of your school? ").title()
        favorite_color = input("What is your favorite color? ").title()
        favorite_food = input("What is your favorite food? ").title()
        class_name = input("What class are you in? ").title()

        print("\n" + " My Information ".center(60, "="))
        print(f"1. My name is {name}")
        print(f"2. I am {age} years old")
        print(f"3. I attend {school}")
        print(f"4. My favorite color is {favorite_color}")
        print(f"5. My favorite food is {favorite_food}")
        print(f"6. I am in {class_name}")

# Example usage:
if __name__ == "__main__":
    user_info = Information()
    user_info.my_information1()
