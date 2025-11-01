# grade calculator

def calculate_grade(mark):
    if mark < 0 or mark > 100:
        return 'Invalid mark. Please enter a value between 0 and 100.'
    elif mark >= 90:
        return 'A'
    elif mark >= 80:
        return 'B'
    elif mark >= 70:
        return 'C'
    elif mark >= 60:
        return 'D'
    else:
        return 'F'


# Program starts here
print('-------------------------------------------------------------------')
print("Welcome to the Grade Calculator Program")
print("Type 'q' anytime to quit.")
print('-------------------------------------------------------------------\n')

while True:
    mark_input = input('Enter Your Mark: ').strip()

    # Exit condition
    if mark_input.lower() == 'q':
        print("Program exited. Goodbye!")
        break
    try:
        mark = int(mark_input)

        # Call the function and show result
        grade = calculate_grade(mark)
        print(f"Your grade is: {grade}\n")

    # Handle invalid (non-integer) input
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

