# Geometry Calculator

class Area:
    """
    A class to calculate the perimeter and area of various geometric shapes.
    Methods:
        - square: Calculates perimeter and area of a square.
        - rectangle: Calculates perimeter and area of a rectangle.
        - triangle: Calculates perimeter and area of a triangle.
        - rhombus: Calculates perimeter and area of a rhombus.
        - kite: Calculates perimeter and area of a kite.
        - parallelogram: Calculates perimeter and area of a parallelogram.
        - circle: Calculates circumference and area of a circle.
        - trapezium: Calculates perimeter and area of a trapezium.
    """

    def square(self):
        """Calculate perimeter and area of a square."""
        length = int(input("Enter the side length of the square: "))
        perimeter = length * 4
        area = length ** 2
        print(f"Perimeter = {perimeter} units.")
        print(f"Area = {area} units^2.")

    def rectangle(self):
        """Calculate perimeter and area of a rectangle."""
        length = int(input("Enter the length of the rectangle: "))
        breadth = int(input("Enter the breadth of the rectangle: "))
        perimeter = 2 * (length + breadth)
        area = length * breadth
        print(f"Perimeter = {perimeter} units.")
        print(f"Area = {area} units^2.")

    def triangle(self):
        """Calculate perimeter and area of a triangle."""
        base = int(input("Enter the base of the triangle: "))
        height = int(input("Enter the height of the triangle: "))
        a = int(input("Enter side a: "))
        b = int(input("Enter side b: "))
        c = int(input("Enter side c: "))
        area = (base * height) / 2
        perimeter = a + b + c
        print(f"Perimeter = {perimeter} units.")
        print(f"Area = {area} units^2.")

    def rhombus(self):
        """Calculate perimeter and area of a rhombus."""
        length = int(input("Enter the side length of the rhombus: "))
        d1 = int(input("Enter diagonal 1: "))
        d2 = int(input("Enter diagonal 2: "))
        perimeter = 4 * length
        area = (d1 * d2) / 2
        print(f"Perimeter = {perimeter} units.")
        print(f"Area = {area} units^2.")

    def kite(self):
        """Calculate perimeter and area of a kite."""
        a = int(input("Enter side a: "))
        b = int(input("Enter side b: "))
        c = int(input("Enter side c: "))
        d = int(input("Enter side d: "))
        d1 = int(input("Enter diagonal 1: "))
        d2 = int(input("Enter diagonal 2: "))
        perimeter = a + b + c + d
        area = (d1 * d2) / 2
        print(f"Perimeter = {perimeter} units.")
        print(f"Area = {area} units^2.")

    def parallelogram(self):
        """Calculate perimeter and area of a parallelogram."""
        a = int(input("Enter side a: "))
        b = int(input("Enter side b: "))
        base = int(input("Enter the base: "))
        height = int(input("Enter the height: "))
        perimeter = 2 * (a + b)
        area = base * height
        print(f"Perimeter = {perimeter} units.")
        print(f"Area = {area} units^2.")

    def circle(self):
        """Calculate circumference and area of a circle."""
        radius = int(input("Enter the radius of the circle: "))
        diameter = radius * 2
        circumference = 2 * (22 / 7) * radius
        area = (22 / 7) * radius ** 2
        print(f"Diameter = {diameter} units.")
        print(f"Circumference = {circumference} units.")
        print(f"Area = {area} units^2.")

    def trapezium(self):
        """Calculate perimeter and area of a trapezium."""
        a = int(input("Enter side a: "))
        b = int(input("Enter side b: "))
        c = int(input("Enter side c: "))
        d = int(input("Enter side d: "))
        h = int(input("Enter the height: "))
        perimeter = a + b + c + d
        area = ((a + b) * h) / 2
        print(f"Perimeter = {perimeter} units.")
        print(f"Area = {area} units^2.")


# Example usage:
if __name__ == "__main__":
    shape_calculator = Area()
    while True:
        print("\nChoose a shape to calculate:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Rhombus")
        print("5. Kite")
        print("6. Parallelogram")
        print("7. Circle")
        print("8. Trapezium")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")
        if choice == "1":
            shape_calculator.square()
            break
        elif choice == "2":
            shape_calculator.rectangle()
            break
        elif choice == "3":
            shape_calculator.triangle()
            break
        elif choice == "4":
            shape_calculator.rhombus()
            break
        elif choice == "5":
            shape_calculator.kite()
            break
        elif choice == "6":
            shape_calculator.parallelogram()
            break
        elif choice == "7":
            shape_calculator.circle()
            break
        elif choice == "8":
            shape_calculator.trapezium()
            break
        elif choice == "9":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
