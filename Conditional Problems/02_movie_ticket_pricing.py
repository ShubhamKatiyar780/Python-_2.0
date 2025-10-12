# Movie Ticket Pricing Program

# Constants for pricing
CHILD_PRICE = 15
ADULT_PRICE = 20
SENIOR_PRICE = 17
DISCOUNT_WEDNESDAY = 2


# Function to categorize age into different groups
def categorize_age(age):
    # Check if age is zero or negative → invalid case
    if age <= 0:
        return "You entered an invalid age.\n"
    elif age < 18:
        return 'Child'
    elif age <= 59:
        return 'Adult'
    elif age <= 130:
        return 'Senior Citizen'
     # If age exceeds 130 → considered unrealistic
    else:
        return "Entered age seems unrealistic. Please try again.\n"
    

# Function to check day-based discount
def check_discount(day):
    return DISCOUNT_WEDNESDAY if day.lower() == 'wednesday' else 0


# Function to verify if the entered day is valid
def verify_day(day):
    valid_days = ['monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    return day.lower() in valid_days

# Function to calculate ticket price
def ticket_pricing(category, discount):
    if category == 'Child':
        base_price = CHILD_PRICE
    elif category == 'Adult':
        base_price = ADULT_PRICE
    elif category == 'Senior Citizen':
        base_price = SENIOR_PRICE
    else:
        return None
    # Apply discount safely (never below 0)
    return max(0, base_price - discount)


# Program starts here
print('-------------------------------------------------------------------')
print("Welcome to the Movie Ticket Pricing Program")
print("Type 'q' anytime to quit.")
print('-------------------------------------------------------------------\n')


# Infinite loop to repeatedly take user input until 'q' is entered
while True:
    age_input = input('Enter Your Age: ').strip()

    # Exit condition
    if age_input.lower() == 'q':
        print("Program exited. Goodbye!")
        break

    day_input = input('For which day would you like to book the ticket?: ').strip()

    # Verify entered day
    if not verify_day(day_input):
        print('Invalid day entered. Please try again.\n')
        continue

    try:
        # Convert input to integer
        age = int(age_input)

        # Get category from the function
        category = categorize_age(age)
        # Invalid case handle
        if category not in ['Child', 'Adult', 'Senior Citizen']:
            print(category)
            continue

        # Get discount
        discount = check_discount(day_input)
        # Get price
        price = ticket_pricing(category, discount)

        # Print result
        print(f"Day: {day_input.capitalize()}")
        print(f"\nCategory: {category}")
        if discount:
            print(f"Ticket price: ${price} (including ${discount} Wednesday discount)\n")
        else:
            print(f"Ticket price: ${price}\n")

        # Handle invalid (non-integer) input
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")