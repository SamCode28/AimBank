class Customer:
    def __init__(self, f_name : str, l_name : str, username : str, password : str):
        self.f_name = f_name
        self.l_name = l_name
        self.username = username
        self.password = password
        self.email = f"{self.username}@bank.com"
        self.balance = 1000.00

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount : float):
        self.balance += amount

    def withdrawal(self):
        while(True):
            try:
                amount = float(input("How much would you like to withdraw?"))

            except ValueError:
                print("Please enter a digit amount. ")
                continue

            else:
                resulting_balance = self.balance - amount

                if(resulting_balance < 0):
                    self.overdraft_warning(resulting_balance)

                else:
                    self.balance -= amount
                    print(f"You have removed {amount} from your account. \n")
                return

    def overdraft_warning(self, resulting_balance : float):
        print(f"\nWarning: This withdrawal will place your account in a negative balance, ${resulting_balance}, which will cause an automatic overdraft fee of $100.")
        while(True):
            try:
                answer = input("Would you like to continue? Y/N ").upper()
            except ValueError:
                print("Please enter 'Y' to continue or 'N' to stop transaction")
                continue
            else:
                if(answer[0] == "Y"):
                    self.balance = resulting_balance - 100
                    print(f"Your new balance is {self.balance}\n")
                else:
                    print("Transaction cancelled.\n")
                return
        
    def __str__(self):
        return f"Your balance is ${self.balance}"