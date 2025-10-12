# Function to categorize age into different groups
def categorize_age(age):
    # Check if age is zero or negative → invalid case
    if age <= 0:
        return "Age cannot be zero or negative. Try again.\n"
    # Age group: Child
    elif age < 13:
        return 'Child'
    # Age group: Teenager
    elif 13 <= age <= 19:
        return 'Teenager'
    # Age group: Adult
    elif 20 <= age <= 59:
        return 'Adult'
    # Age group: Senior (realistic upper bound is set to 130)
    elif 60 <= age <= 130:
        return 'Senior'
    # If age exceeds 130 → considered unrealistic
    else:
        return "Entered age seems unrealistic. Please try again.\n"


# Program introduction
print("Age Categorization Program")
print("Type 'q' anytime to quit.\n")

# Infinite loop to repeatedly take user input until 'q' is entered
while True:
    user_input = input('Enter Your Age: ').strip()
    
    # Exit condition
    if user_input.lower() == 'q':
        print("Program exited. Goodbye!")
        break

    try:
        # Convert input to integer
        age = int(user_input)
        
        # Get category from the function
        category = categorize_age(age)
        
        # Display result
        print(f'You are categorized as: {category}\n')
    
    # Handle invalid (non-integer) input
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
