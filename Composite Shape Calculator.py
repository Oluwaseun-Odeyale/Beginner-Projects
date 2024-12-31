import math

class CompositeShape:
    """
    A class to calculate the Total Surface Area (TSA), Curved Surface Area (CSA),
    and Volume of various 3D shapes.
    """

    def cube(self):
        """Calculate TSA and Volume of a cube."""
        length = self.get_positive_input("Enter the side length of the cube: ")
        tsa = 6 * (length ** 2)
        volume = length ** 3
        print(f"Total Surface Area (TSA) = {tsa} units^2.")
        print(f"Volume = {volume} units^3.")

    def cuboid(self):
        """Calculate TSA and Volume of a cuboid."""
        length = self.get_positive_input("Enter the length of the cuboid: ")
        breadth = self.get_positive_input("Enter the breadth of the cuboid: ")
        height = self.get_positive_input("Enter the height of the cuboid: ")
        tsa = 2 * ((length * breadth) + (breadth * height) + (length * height))
        volume = length * breadth * height
        print(f"Total Surface Area (TSA) = {tsa} units^2.")
        print(f"Volume = {volume} units^3.")

    def cylinder(self):
        """Calculate TSA, CSA, and Volume of a cylinder."""
        radius = self.get_positive_input("Enter the radius of the cylinder: ")
        height = self.get_positive_input("Enter the height of the cylinder: ")
        tsa = 2 * math.pi * radius * (height + radius)
        volume = math.pi * (radius ** 2) * height
        csa = 2 * math.pi * radius * height
        print(f"Total Surface Area (TSA) = {tsa:.2f} units^2.")
        print(f"Curved Surface Area (CSA) = {csa:.2f} units^2.")
        print(f"Volume = {volume:.2f} units^3.")

    def cone(self):
        """Calculate TSA, CSA, and Volume of a cone."""
        radius = self.get_positive_input("Enter the radius of the cone: ")
        slant_height = self.get_positive_input("Enter the slant height of the cone: ")
        height = self.get_positive_input("Enter the height of the cone: ")
        tsa = math.pi * radius * (slant_height + radius)
        volume = (1 / 3) * math.pi * (radius ** 2) * height
        csa = math.pi * radius * slant_height
        print(f"Total Surface Area (TSA) = {tsa:.2f} units^2.")
        print(f"Curved Surface Area (CSA) = {csa:.2f} units^2.")
        print(f"Volume = {volume:.2f} units^3.")

    def sphere(self):
        """Calculate TSA and Volume of a sphere."""
        radius = self.get_positive_input("Enter the radius of the sphere: ")
        tsa = 4 * math.pi * (radius ** 2)
        volume = (4 / 3) * math.pi * (radius ** 3)
        print(f"Total Surface Area (TSA) = {tsa:.2f} units^2.")
        print(f"Volume = {volume:.2f} units^3.")

    def hemisphere(self):
        """Calculate TSA and Volume of a hemisphere."""
        radius = self.get_positive_input("Enter the radius of the hemisphere: ")
        tsa = 3 * math.pi * (radius ** 2)
        volume = (2 / 3) * math.pi * (radius ** 3)
        print(f"Total Surface Area (TSA) = {tsa:.2f} units^2.")
        print(f"Volume = {volume:.2f} units^3.")

    @staticmethod
    def get_positive_input(prompt):
        """Prompt the user for a positive numeric input."""
        while True:
            try:
                value = float(input(prompt))
                if value > 0:
                    return value
                else:
                    print("The value must be positive. Try again.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    shape_calculator = CompositeShape()
    print("Select a shape to calculate:")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Cylinder")
    print("4. Cone")
    print("5. Sphere")
    print("6. Hemisphere")

    while True:
        choice = input("Enter your choice (1-6, or 'q' to quit): ").strip().lower()
        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break
        elif choice == '1':
            shape_calculator.cube()
            break
        elif choice == '2':
            shape_calculator.cuboid()
            break
        elif choice == '3':
            shape_calculator.cylinder()
            break
        elif choice == '4':
            shape_calculator.cone()
            break
        elif choice == '5':
            shape_calculator.sphere()
            break
        elif choice == '6':
            shape_calculator.hemisphere()
            break
        else:
            print("Invalid choice. Please select a valid option.")
