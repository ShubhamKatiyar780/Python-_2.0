# Define Customer class
class Customer:
    # Constructor to initialize customer object
    def __init__(self, name, gender, address):
        self.name = name          # Set customer name
        self.gender = gender      # Set customer gender
        self.address = address    # Set address (Aggregation - HAS-A relationship)

    def print_address(self):
        print(f"City: {self.address.get_city()}")
        print(f"State: {self.address.state}")
        print(f"Country: {self.address.country}")

    def edit_profile(self, new_name, new_city, new_state, new_country):
        self.name = new_name
        self.address.edit_address(new_city, new_state, new_country)


# Define Address class
class Address:
    # Constructor to initialize address object
    def __init__(self, city, state, country):
        self.__city = city          # Set city
        self.state = state        # Set state
        self.country = country    # Set country

    def get_city(self):
        return self.__city
    
    def edit_address(self, new_city, new_state, new_country):
        self.__city = new_city
        self.state = new_state
        self.country = new_country



# Create an Address object
addr1 = Address("Noida", "UP", "INDIA")  # city=Noida, state=UP, country=INDIA

# Create a Customer object with the address (Aggregation)
cust1 = Customer("Shubham", "Male", addr1)  # name=Shubham, gender=Male, address=addr1

print(cust1.name)
cust1.print_address()

cust1.edit_profile('Rajat', 'Kanpur', 'California', 'United State')

print(cust1.name)
cust1.print_address()