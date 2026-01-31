# Define a utility class for math operations
class MathOperation:
    @staticmethod
    def add(x, y):
        """
        Static method to add two numbers.
        Does not depend on instance or class variables.
        """
        return x + y

# Call the static add method directly using the class name
result = MathOperation.add(5, 6)

# Print the result of addition
print(f"Sum: {result}")




# Define a utility class for weather-related conversions
class WeatherUtils:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """
        Static method to convert Celsius temperature to Fahrenheit.
        Formula: (Celsius × 9/5) + 32
        No instance or class data used.
        """
        return (celsius * 9 / 5) + 32

# Temperature in Celsius
temp_c = 25

# Convert to Fahrenheit using the static method
temp_f = WeatherUtils.celsius_to_fahrenheit(temp_c)

# Print the converted temperature
print(f"{temp_c}°C is equal to {temp_f}°F")

