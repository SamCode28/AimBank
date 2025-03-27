from customer import Customer

customer_options1 = """Enter a digit to choose from the following options:
[1] Login
[2] Create Account
[3] Quit
"""
customer_options2 = """    [1] Show Balance
    [2] Deposit
    [3] Withdrawal
    [4] Print Statement
    [5] Email Statement
    [6] Quit
"""

class StateBank: 
    def __init__(self, bank_users : dict):
        self.customer_logged_in=None
        self.bank_users = bank_users

    def start(self):
        print("\nWelcome to State Bank!\n")

        while True:
            try:
                print(customer_options1)            
                response = int(input("Enter Digit: "))

            except ValueError:
                print("\nThe number entered must be 1-3, please try again.\n")
                continue

            else:
                if (response < 1 or response > 3):
                    print("\nNumber out of range. The number entered must be between 1-3.\n")
                    continue
                
            if(response == 1):
                self.sign_in()
            elif(response == 2):
                self.new_user()
            else:
                print("Goodbye!\n")
                return
            
    def customer_logged_in_prompt(self):
        while(True):
            try:
                print(customer_options2)
                response = int(input("Enter Digit: "))
            except ValueError:
                print("Invalid number, please try again")
                continue
            else:
                if(response < 0 or response > 6):
                    print("The number entered must be 1-6.  Please try again.")

            if(response == 1):
                print(f"\nYou have ${self.customer_logged_in.balance} in your account.\n")

            elif(response == 2):
                while(True):
                    try:
                        amount = float(input("How much would you like to deposit? "))

                    except ValueError:
                        print("Amount to deposit must be a digit.")
                        continue

                    else:
                        self.customer_logged_in.deposit(amount)
                        print(f"Your account has been credited with {amount}.\n")
                        break

            elif(response == 3):
                self.customer_logged_in.withdrawal()

            elif(response == 4):
                print(self.customer_logged_in)

            elif(response == 5):
                self.email_statement()

            elif(response == 6):
                print("Returning to main menu.\n")
                return                
    
    def email_statement(self):
        print(f"An email has been sent to {self.customer_logged_in.email}.\n")
            
    def sign_in(self):
        attempts = 5
        while(attempts > 0):
            username_found = False
            username = input("Please enter your username: ")
  
            for value in self.bank_users.values():
                if (value.username == username):
                    username_found = True

            if(username_found == False):
                attempts -= 1
                print(f"That username does not exist.  Please enter a valid username.  You have {attempts} remaining before lockout.\n")
                continue
            
            #If username found, search for valid password
            password = input("Please enter your password: ")
            for value in self.bank_users.values():
                if (value.password == password):
                    self.customer_logged_in = value
                    
                    print(f"\nWelcome, {value.f_name}!  How can I help you?")
                    self.customer_logged_in_prompt()
                    return
                    
            attempts -= 1
            print(f"That password does not exist. You have {attempts} remaining before lockout.\n")
            
        print("Login attempts exceded.  Returning to main menu\n")

    def new_user(self):
        print("\nCreating new user...")
        #List of variables required
        f_name = None
        l_name = None
        username = None
        password = None

        #Get first and last name without any extra spaces
        f_name = input("Please enter your first name: ").title().strip()
        l_name = input("Please enter your last name: ").title().strip()

        #Username is first letter of name followed by last name for consistency
        username = (f_name[0] + l_name).lower()

        print(f"\nWelcome, {f_name}!  The username '{username}' has automatically generated for you.")

        #Password must be:
        # 6-12 characters
        # 1 lowercase
        # 1 uppoercase
        # 1 digit
        # 1 special character of (!,@,?,#,$,%,-,&,*,=)

        #Used to check if entered password matched one of the following special characters
        special_chars = ("!","@","?","#","$","%","-","&","*","=")

        while True:
            password = input(""" 
Please enter a password with the following requirements:
    6-12 Characters
    At least 1 uppercase
    At least 1 lowercase
    At least 1 digit
    At least 1 of the following special charaecers...
    ("!","@","?","#","$","%","-","&","*","=")
                             
Password: """)

            #Check length of password, restart loop if length parameters not met
            if (len(password)) < 6 or (len(password)) > 12:
                print("Password must be between 6-12 characters")
                continue

            #All variables needed to pass
            upper = False
            lower = False
            digit = False
            special = False

            for character in password:
                if(character.isdigit()):
                    digit =  True
                elif(character.isupper()):
                    upper = True
                elif(character.islower()):
                    lower = True
                elif(character in special_chars):
                    special = True

            if(upper and lower and digit and special):
                password_confirm = input("Success! Please re-enter password to confirm: ")
            else:
                continue

            #If both passwords match, create new user, break out of function
            if(password == password_confirm):
                new_user = Customer(f_name, l_name, username, password)
                self.bank_users.update({new_user.f_name + " " + new_user.l_name : new_user})
                print(f"\nAccount succesfully created!  Welcome to State Bank, {f_name} {l_name}!  To access your bank, please log in.\n")
                return
            
            #Send back to create a password
            else:
                print("Your passwords do not match. Please try again.")
                continue
