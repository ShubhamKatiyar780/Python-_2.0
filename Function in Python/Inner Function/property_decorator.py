class Circle:
    def __init__(self, radius):
        # Constructor to initialize the circle with a given radius
        # The radius is stored in a "protected" variable _radius
        self._radius = radius

    @property
    def radius(self):
        """
        Getter method for radius.
        Allows access to the private _radius variable using the dot notation.
        Example: c.radius
        """
        return self._radius

    @radius.setter
    def radius(self, value):
        """
        Setter method for radius.
        Ensures the radius cannot be set to a negative value.
        Example: c.radius = 10
        """
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def area(self):
        """
        Read-only property to calculate the area of the circle.
        Formula: π * r^2
        Example: c.area
        """
        pi = 3.14159
        return pi * (self._radius ** 2)


# ----------- Example Usage -----------

# Create a circle object with radius 5
c = Circle(5)

# Print the initial radius using the getter
print("Initial radius:", c.radius)

# Print the initial area of the circle
print("Initial area: ", c.area)

# Update the radius using the setter
c.radius = 10

# Print the updated radius
print("Updated radius:", c.radius)

# Print the new area after radius update
print("Updated area: ", c.area)
