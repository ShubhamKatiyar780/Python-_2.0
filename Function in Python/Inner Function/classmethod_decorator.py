class Circle:
    def __init__(self, radius):
        """Initialize the Circle with a given radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the Circle."""
        return 3.14159 * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, diameter):
        """
        Create a Circle instance using the diameter.
        This is an alternative constructor.
        """
        radius = diameter / 2
        return cls(radius)


# Creating Circle using radius
circle1 = Circle(10)
print("Circle 1:")
print("  Radius:", circle1.radius)
print("  Area:", circle1.area())

# Creating Circle using diameter
circle2 = Circle.from_diameter(20)
print("\nCircle 2 (created from diameter):")
print("  Radius:", circle2.radius)
print("  Area:", circle2.area())


print(Circle.from_diameter.__doc__)

