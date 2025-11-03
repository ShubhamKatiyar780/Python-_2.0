class Google:

    def __init__(self, name, email, password, device, active = False):
        # Initialize user account with private attributes
        self.__name = name
        self.__email = email
        self.__password = password
        self.__device = device
        self.__active = active
    
    def login(self, email, password, device):
        # Check if device is recognized
        if device != self.__device:
            raise LogoutRequired('Unrecognized device detected.')
        
        # Validate email and password
        if email != self.__email or password != self.__password:
            raise AuthenticationError('Invalid email or password.')
        
        # Login successful
        print("Login Successful!")
        print(f"Welcome, {self.__name}")
        return (self.__active == True)

    def logout(self):
        # End current session if active
        if self.__active:
            self.__active = False
            return ("Logged out successfully.")
        else:
            return ("No active session found.")


class SecurityError(Exception):
    # Base class for security-related exceptions
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class LogoutRequired(SecurityError):
    """Raised when a critical security breach requires logout."""
    pass


class AuthenticationError(SecurityError):
    """Raised when credentials are incorrect."""
    pass


if __name__ == "__main__":
    # Create test user
    user1 = Google('shubham', 'sh@gmail.com', 'Shu@123', 'android')

    # Attempt login with error handling
    try:
        user1.login('s@gmail.com', 'Shu@123', 'android')
    except LogoutRequired as e:
        # Handle unrecognized device
        print(f"{e.message}")
        print(user1.logout())
    except AuthenticationError as e:
        # Handle wrong credentials
        print(f"{e.message}")
    else:
        # Code that runs if login succeeds
        print('Access granted to account.')
    finally:
        # Always runs regardless of login outcome
        print('Database connection closed.')