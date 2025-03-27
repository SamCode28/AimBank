from main import bank_users
from customer import Customer

class Signup:

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
                bank_users.update({new_user.f_name + " " + new_user.l_name : new_user})
                print(f"\nAccount succesfully created!  Welcome to State Bank, {f_name} {l_name}!  To access your bank, please log in.\n")
                return
            
            #Send back to create a password
            else:
                print("Your passwords do not match. Please try again.")
                continue