import pwinput
class RegistrationDetails:
    def userRegister(self):
        print("-----User Registration-----")
        name = input("Enter Your Name: ")

        while True:
            email = input("Enter Your Email-Id: ")
            if self.validationEmail(email):
                if self.exitanceOfEmail(email):
                    print("Your Email-Id is already registered. Please try a different one.")
                else:
                    print("Your Email-id is valid.")
                    break
            else:
                print("Please provide a valid Email-ID ending with '@gmail.com'.")
        
        # self.exitanceOfEmail(email)
        while True:
            password = pwinput.pwinput("Enter Your Password: ", mask='*')
            if self.validataionPassword(password):
                print("Your Password is valid.")
                break
            else:
                print("Password must be at least 8 characters long.")

        security_answer = self.securityQuestion()
        encrypted_security_answer = self.encryptedSecurityAnswer(security_answer)
        encrycted_password = self.encryptedPassword(password)

        file = open('RegistrationLogin.csv' , 'a')
        file.write(f"{name},{email},{encrycted_password},{encrypted_security_answer}\n")
        file.close()
        print("Registration successful!\n")


    def exitanceOfEmail(self, email):
        try:
            file = open('RegistrationLogin.csv' , 'r')
            for line in file:
                details = line.strip().split(',')
                stored_email = details[1]
                if stored_email == email:
                    file.close()
                    return True
                return False
        except FileNotFoundError:
            print("File Not Fount.")

    def securityQuestion(self):
        while True:
            print("------------Security Question------------")
            print("1. What was the name of your first pet?")
            print("2. What is your favorite movie?")
            print("3. What was the name of your first grade teacher?")
            choice = int(input("Select Your Security Question: "))
            if choice in [1, 2, 3]:
                answer = pwinput.pwinput("Enter Your Answer: ", mask='*')
                return answer
                break
            else:
                print("Invalid Your Choice.")

    def encryptedSecurityAnswer(self, security_answer):
        hash_value = 100
        for char in security_answer:
            hash_value = ((hash_value << 5) + hash_value) +ord(char)
        return str(hash_value)


    def validationEmail(self, email):
        if email.endswith("@gmail.com"):
            return True
        return False
    

    def validataionPassword(self, password):
        capital_lettar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        small_letter = "abcdefghijklmnopqrstuvwxyz"
        special_letter = "!@#$%^&*"
        digits = "0123456789"
        a,b,c,d = 0,0,0,0
        if (len(password) >= 8):
            for i in password:
                if (i in capital_lettar):
                    a += 1
                if (i in small_letter):
                    b += 1
                if (i in digits):
                    c += 1
                if (i in special_letter):
                    d += 1
            if (a>=1 and b>=1 and c>=1 and d>=1):
                return True
            else:
                print("Your Password is not Valid.")
                print("Password must include: ")
                if a == 0:
                    print("- At least one Capital Letter (A-Z).")
                if b == 0:
                    print("- At least one Small Letter (a-z).")
                if c == 0:
                    print("- At least one Numeric Digit (0-9).")
                if d == 0:
                    print("- At least one Special Character (!@#$%^&*).")
                return False
            
    
    def encryptedPassword(self, password,):
        hash_value = 5000
        for char in password:
            hash_value = ((hash_value << 5) + hash_value) +ord(char)
        return str(hash_value)
        

    def logIn(self, email, password):
        try:
            file = open('RegistrationLogin.csv' , 'r')
            encrypted_password = self.encryptedPassword(password)
            for line in file:
                details = line.strip().split(',')
                stored_email = details[1]
                stored_password = details[2]
                if stored_email == email and stored_password == encrypted_password:
                    file.close()
                    return True
                return False
        except FileNotFoundError:
            print("File Not Fount.")


    def stockMarketData(self):
        try:
            while True:
                import requests
                from datetime import datetime
                print("---------Welcome in Stock Market---------")
                self.symbol = input("Enter the Ticker Symbol or Company Name: ")
                url = 'https://www.alphavantage.co/query'
                params = {
                    'function': 'TIME_SERIES_INTRADAY',
                    'symbol': self.symbol,
                    'interval': '1min',
                    # 'apikey': 'ac481cebf14d4998ba10b950922844de',
                    'apikey': '3fed8ee23amsh0a1d767b9bfaa5cp190e62jsn41ded594646a',
                    'outputsize': 'compact'
                }
                response = requests.get(url, params=params)
                data = response.json()
                if "Time Series (1min)" in data:
                    current_date = str(datetime.now().date())
                    latest_time = next(iter(data['Time Series (1min)']))
                    latest_data = data['Time Series (1min)'][latest_time]
                    stock_info = {
                        'Date': current_date,
                        'Current Price': latest_data['1. open'],
                        'Open Price': latest_data['1. open'],
                        'High Price': latest_data['2. high'],
                        'Low Price': latest_data['3. low'],
                        'Previous Close': latest_data['4. close'],
                        'Volume': latest_data['5. volume']
                    }
                    print("-----Stock Market Data-----")
                    for key, value in stock_info.items():
                        print(f"{key}: {value}")
                    print(header)
                else:
                    print("Data not Fetched. Please Check the Ticker Symbol or Company Name.\n")

                choice_for_logout = input("Do you want Logout (Yes or No): ").strip().lower()
                if choice_for_logout == "yes":
                    print("Logout Successful!\n")
                    break
        except requests.ConnectionError:
            print("No Internet. Please check your internet connection.")
        except KeyError:
            print("Unexpected data format received. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    def countAttempts(self):
        max_attempts = 5
        attempts = 0
        from datetime import datetime
        while max_attempts > attempts:
            print("-----------User LogIn-----------")
            while True:
                email = input("Enter Your Registered Email-Id: ")
                if self.validationEmail(email):
                    print("Your Email-id is valid.")
                    break
                else:
                    print("Please provide a valid Email-ID ending with '@gmail.com'.")
            while True:
                password = pwinput.pwinput("Enter Your Password: ", mask='*')
                if self.validataionPassword(password):
                    print("Your Password is Valid.")
                    break
                else:
                    print("Password must be at least 8 characters long.")

            if self.logIn(email, password):
                print("Login successful!")
                print(header)
                self.stockMarketData()
                break
            else:
                attempts += 1
                print("Invalid email or password.")
                print(f"Login failed. {max_attempts - attempts} attempts left!")
        self.current_time = datetime.now()
        if max_attempts == attempts :
            lockout_time = self.current_time.hour + 24
            print(f"Too many attempts. Try after {lockout_time} hours.\n")


    def forgotPassword(self):
        print("---------Forgot Password---------")
        while True:
            email = input("Enter Your Registered Email-Id: ")
            if self.validationEmail(email):
                print("Your Email-id is valid.")
                break
            else:
                print("Please provide a valid Email-ID ending with '@gmail.com'.")
        
        security_answer = self.securityQuestion()
        encrypted_security_answer = self.encryptedSecurityAnswer(security_answer)
        file = open('RegistrationLogin.csv', 'r')
        for k in file:
            details = k.strip().split(',')
            stored_email = details[1]
            stored_security_answer = details[3]
            if stored_email == email and stored_security_answer == encrypted_security_answer:
                print("Email found. You can reset your password.")
                while True:
                    new_password = pwinput.pwinput("Enter Your New Password: ", mask='*')
                    confirm_new_password = pwinput.pwinput("Confirm Your New Password: ",mask='*')
                    if new_password == confirm_new_password:
                        if self.validataionPassword(new_password):
                            self.updatePassword(email,new_password)
                            print("Your New Password is Valid.")
                            print("Password updated successfully!")
                            break
                        else:
                            print("New Password must be at least 8 characters long.")
                    else:
                        print("Confirm Passwords do not match. Please try again.")
                        file.close()
                return            
        print("Email not found. Please check your email-id and try again.\n")


    def updatePassword(self,email,new_password):
        encrypted_new_password = self.encryptedPassword(new_password)
        file = open('RegistrationLogin.csv', 'r')
        lines = file.readlines()
        file.close()
        file = open('RegistrationLogin.csv','w')
        for k in lines:
            details = k.strip().split(',')
            stored_email = details[1]
            if stored_email == email:
                details[2] = encrypted_new_password
                update_password = (','.join(details) + '\n')
            file.write(update_password)
        file.close()


obj = RegistrationDetails()
while True:
    header = "-"*65
    print(header)
    print("-----Stock Market Data Console Application with Secure Login-----")
    print(header)
    print("1. User Registration")
    print("2. User LogIn")
    print("3. Forgot Password")
    print("4. Exit")
    choice = int(input("Select Your Choice: "))
    match choice:
        case 1:
            obj.userRegister()
        case 2:
            obj.countAttempts()
        case 3:
            obj.forgotPassword()
        case 4:
            print("Exit Your Application !")
            break
        case _:
            print("Invalid Choice")