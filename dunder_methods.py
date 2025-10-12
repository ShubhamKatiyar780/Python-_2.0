# Define a class named Fraction to represent fractional numbers
class Fraction:
    # Special method (constructor) called when creating a new Fraction instance
    def __init__(self, numerator, denominator):
        # Check if denominator is zero, which is mathematically invalid
        if denominator == 0:
            # Raise an error with a descriptive message
            raise ValueError("Denominator cannot be zero.")
        # Assign the numerator parameter to the instance variable
        self.numerator = numerator
        # Assign the denominator parameter to the instance variable
        self.denominator = denominator

    # Special method to define the + operator behavior for Fraction objects
    def __add__(self, other):
        # Check if the other object is also a Fraction instance
        if isinstance(other, Fraction):
            # Calculate new numerator using cross-multiplication formula
            new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            # Calculate new denominator by multiplying denominators
            new_denominator = self.denominator * other.denominator
            # Return a new Fraction object with the calculated values
            return Fraction(new_numerator, new_denominator)
        
    # Special method to define the - operator behavior for Fraction objects
    def __sub__(self, other):
        # Check if the other object is also a Fraction instance
        if isinstance(other, Fraction):
            # Calculate new numerator using cross-multiplication formula
            new_numerator = (self.numerator * other.denominator) - (self.denominator * other.numerator)
            # Calculate new denominator by multiplying denominators
            new_denominator = (self.denominator * other.denominator)
            # Return a new Fraction object with the calculated values
            return Fraction(new_numerator, new_denominator)
        # Return NotImplemented if other is not a Fraction
        return NotImplemented
    
    # Special method to define the * operator behavior for Fraction objects
    def __mul__(self, other):
        # Check if the other object is also a Fraction instance
        if isinstance(other, Fraction):
            # Multiply numerators for new numerator
            new_numerator = self.numerator * other.numerator
            # Multiply denominators for new denominator
            new_denominator = self.denominator * other.denominator
            # Return a new Fraction object with the calculated values
            return Fraction(new_numerator, new_denominator)
        # Return NotImplemented if other is not a Fraction
        return NotImplemented
    
    # Special method to define the / operator behavior for Fraction objects
    def __truediv__(self, other):
        # Check if the other object is also a Fraction instance
        if isinstance(other, Fraction):
            # Check if dividing by zero (numerator of other fraction is zero)
            if other.numerator == 0:
                # Raise an error with a descriptive message
                raise ValueError("Cannot divide by a fraction with a numerator of zero.")
            # Division of fractions is multiplication by reciprocal
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            # Return a new Fraction object with the calculated values
            return Fraction(new_numerator, new_denominator)
        # Return NotImplemented if other is not a Fraction
        return NotImplemented

    # Special method to define the string representation of the object (user-friendly)
    def __str__(self):
        # Return a string in the format "numerator/denominator"
        return (f"{self.numerator}/{self.denominator}")

    # Special method to define the official string representation of the object
    def __repr__(self):
        # Return a more detailed string representation
        return f"Fraction: ({self.numerator}/{self.denominator})"
    
    # Special method to define the == operator behavior for Fraction objects
    def __eq__(self, other):
        # Check if the other object is also a Fraction instance
        if isinstance(other, Fraction):
            # Fractions are equal if cross-products are equal (a/b = c/d if a*d = b*c)
            return (self.numerator * other.denominator) == (other.numerator * self.denominator)
        # Return NotImplemented if other is not a Fraction
        return NotImplemented


# Create a Fraction object with numerator 3 and denominator 4
obj = Fraction(3, 4)
# Create another Fraction object with numerator 2 and denominator 5
obj2 = Fraction(2, 5)
# Test equality between the two fractions and print the result
print(obj + obj2)