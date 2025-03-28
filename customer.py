class Customer:
    def __init__(self, f_name : str, l_name : str, username : str, password : str):
        self.f_name = f_name
        self.l_name = l_name
        self.username = username
        self.password = password
        self.email = f"{self.username}@bank.com"
        self.balance = 1000.00

        #For print statement
        self.initial_balance = 1000.00
        self.deposits_made = []
        self.withdrawals_made = []
        self.overdraft_fees = 0.0

    #DEPOSIT METHODS
    
    def deposit(self, amount : float):
        self.balance += amount
        self.add_deposit(amount)
    
    def add_deposit(self, deposit : float):
        self.deposits_made.append(deposit)

    def get_deposits_total(self):
        return self.add_list_items(self.deposits_made)
    
    # WITHDRAWAL METHODS

    def withdrawal(self):
        while(True):
            try:
                amount = float(input("How much would you like to withdraw? "))

            except ValueError:
                print("Please enter a digit amount. ")
                continue

            else:
                #Used to check balance outcome without changing balance
                resulting_balance = self.balance - amount

                if(resulting_balance < 0):
                    self.overdraft_warning(resulting_balance, amount)

                else:
                    self.balance -= amount
                    self.add_withdrawal(amount)
                    print(f"You have removed {amount} from your account. \n")
                return

    def overdraft_warning(self, resulting_balance : float, amount : float = 0):
        print(f"\nWarning: This withdrawal will place your account in a negative balance, ${resulting_balance}, which will cause an automatic overdraft fee of $100.")
        while(True):
            try:
                answer = input("Would you like to continue? (Y/N) ").upper()
            except ValueError:
                print("Please enter 'Y' to continue or 'N' to stop transaction")
                continue
            else:
                if(answer[0] == "Y"):
                    self.add_withdrawal(amount)
                    self.add_overdraft_fee()
                    self.balance = resulting_balance - 100
                    print(f"Your new balance is {self.balance}\n")
                else:
                    print("Transaction cancelled.\n")
                return

    def add_withdrawal(self, withdrawal : float):
        self.withdrawals_made.append(withdrawal)

    def get_withdrawals_total(self):
        return self.add_list_items(self.withdrawals_made)
    
    #OVERDRAFT METHODS

    def add_overdraft_fee(self):
        self.balance -= 100
        self.overdraft_fees += 100

    #MISC METHODS

    def add_list_items(self, list : list):
        total = 0
        for item in list:
            total += item
        return total
        
    def __str__(self):
        return f"Your balance is ${self.balance}"