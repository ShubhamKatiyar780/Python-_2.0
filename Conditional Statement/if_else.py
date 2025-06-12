# --------------------------
# If Conditional Statement
# --------------------------
age = 20
if age >= 18:
    print("Eligible to vote.")  # Executes because age is 20

# Short Hand if (single-line if statement)
age = 19
if age > 18: print("Eligible to Vote.")  # Executes because age is greater than 18


# --------------------------
# If-else Conditional Statements
# --------------------------
age = 10
if age <= 12:
    print("Travel for free.")  # Executes because age is less than or equal to 12
else:
    print("Pay for ticket.")

# Short Hand if-else (ternary operator)
marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")  # Outputs: Result: Pass


# --------------------------
# elif Statement (multiple conditions)
# --------------------------
age = 25
if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")  # Executes because age is 25
else:
    print("Adult.")


# --------------------------
# Nested if..else Conditional Statements
# --------------------------
age = 70
is_member = True
if age >= 60:
    if is_member:
        print("30% senior discount!")  # Executes because age >= 60 and is_member is True
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")
