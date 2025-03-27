from main import bank_users
from signup import Signup

class Bank: 
    customer_logged_in=None

    def opening_message(self):
        print("\nWelcome to State Bank!\n")

        while True:
            try:
                response = int(input("""Enter a digit to choose from the following options:
    [1] Login
    [2] Create Account
    [3] Quit
              
Enter Digit: """))

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
                signup = Signup()
                signup.new_user()
            else:
                print("Goodbye!\n")
                return
            
    def customer_logged_in_prompt(self):
        while(True):
            try:
                response = int(input("""    [1] Show Balance
    [2] Deposit
    [3] Withdrawal
    [4] Print Statement
    [5] Email Statement
    [6] Quit
                                     
Enter Digit:"""))
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
                self.withdrawal()

            elif(response == 4):
                print(self.customer_logged_in)

            elif(response == 5):
                self.email_statement()

            elif(response == 6):
                print("Returning to main menu.\n")
                return        

    def withdrawal(self):
        if(self.customer_logged_in.get_balance() <= 300):
            print(f"Warning: Your account is at ${self.customer_logged_in.get_balance()}.  Withdrawing below this will cause an automatic overdraft fee of $100")
        while(True):
            try:
                amount = float(input("How much would you like to withdraw?"))
            except ValueError:
                print("Please enter a digit amount. ")
                continue
            else:
                self.customer_logged_in.withdrawal(amount)
                print(f"You have removed {amount} from your account. \n")
                break
    
    def email_statement(self):
        print(f"An email has been sent to {self.customer_logged_in.email}.\n")
            
    def sign_in(self):
        attempts = 5
        while(attempts > 0):
            username_found = False
            username = input("Please enter your username: ")
  
            for value in bank_users.values():
                if (value.username == username):
                    username_found = True

            if(username_found == False):
                attempts -= 1
                print(f"That username does not exist.  Please enter a valid username.  You have {attempts} remaining before lockout.\n")
                continue
            
            #If username found, search for valid password
            password = input("Please enter your password: ")
            for value in bank_users.values():
                if (value.password == password):
                    self.customer_logged_in = value
                    
                    print(f"\nWelcome, {value.f_name}!  How can I help you?")
                    self.customer_logged_in_prompt()
                    return
                    
            attempts -= 1
            print(f"That password does not exist. You have {attempts} remaining before lockout.\n")
            
        print("Login attempts exceded.  Returning to main menu\n")
