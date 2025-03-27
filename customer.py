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

    def withdrawal(self, amount :float):
        self.balance -= amount

        if(self.balance < 0 and amount > 0):
            self.balance -= 100
        
    def __str__(self):
        return f"Your balance is ${self.balance}"